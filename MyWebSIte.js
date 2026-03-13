import React, { useState, useEffect, useRef } from 'react';

// Main App Component - Default Export
const App = () => {
  // 1. Dark Mode State and Persistence (using localStorage)
  const [darkMode, setDarkMode] = useState(() => {
    const savedMode = localStorage.getItem('portfolio-dark-mode');
    return savedMode === null ? true : savedMode === 'true';
  });

  useEffect(() => {
    // Save dark mode preference to localStorage
    localStorage.setItem('portfolio-dark-mode', darkMode);
    if (darkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [darkMode]);


  // Simple custom hook to handle element visibility for 'in view' animation simulation
  const useInView = (options) => {
    const ref = useRef(null);
    const [inView, setInView] = useState(false);

    useEffect(() => {
      const observer = new IntersectionObserver(([entry]) => {
        if (entry.isIntersecting) {
          setInView(true);
          // Disconnect observer once element is visible for a one-time animation
          observer.unobserve(entry.target);
        }
      }, options);

      if (ref.current) {
        observer.observe(ref.current);
      }

      return () => {
        if (ref.current) {
          observer.unobserve(ref.current);
        }
      };
    }, [options]);

    return [ref, inView];
  };

  // --- Reusable Components for Structure and Animation ---

  const SectionHeader = ({ title, colorClass }) => {
    return (
      <h2 className={`text-4xl sm:text-5xl font-extrabold mb-12 relative pb-2 inline-block ${colorClass}`}>
        {title}
        {/* Animated underline. bg-current inherits the text color. */}
        <span className="absolute left-0 bottom-0 w-1/2 h-1 bg-current rounded-full transition-all duration-700"></span>
      </h2>
    );
  };

  const AnimatedCard = ({ children, delay = 0 }) => {
    // Detect visibility using the custom hook
    const [ref, inView] = useInView({ threshold: 0.1 });

    return (
      <div
        ref={ref}
        className={`bg-white p-6 rounded-xl shadow-xl dark:bg-gray-800 transition-all duration-700 ease-out transform
          ${inView ? 'translate-y-0 opacity-100' : 'translate-y-10 opacity-0'}
          hover:shadow-2xl hover:scale-[1.02] cursor-pointer dark:hover:shadow-blue-500/30`}
        // Apply staggering delay only when entering view
        style={{ transitionDelay: inView ? `${delay}ms` : '0ms' }}
      >
        {children}
      </div>
    );
  };

  const DarkModeToggle = ({ darkMode, setDarkMode }) => (
    <button
      onClick={() => setDarkMode(!darkMode)}
      className="p-2 rounded-full text-gray-500 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-700 transition duration-300"
      aria-label="Toggle dark mode"
    >
      {darkMode ? (
        // Sun icon for switching to Light Mode
        <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
      ) : (
        // Moon icon for switching to Dark Mode
        <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path></svg>
      )}
    </button>
  );

  // --- Skill Icons (Inline SVG) ---

  const PythonIcon = () => (
    <svg className="w-10 h-10 mx-auto mb-2 text-blue-500 dark:text-yellow-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
      <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm2.5 13c0 .83-.67 1.5-1.5 1.5H11v-3h1.5c.83 0 1.5.67 1.5 1.5zm-3.5-6h-1.5V9h1.5v1.5zm.5-3.5c0-.83.67-1.5 1.5-1.5H13v3h-1.5c-.83 0-1.5-.67-1.5-1.5zM11 15h1.5v1.5H11V15zM8 10.5v1.5h1.5v-1.5H8zm0-3v1.5h1.5V7.5H8zm3.5 1.5c0-.83-.67-1.5-1.5-1.5h-1.5V9h1.5c.83 0 1.5.67 1.5 1.5zM13 15v1.5h1.5v-1.5H13zm.5-3.5c0-.83-.67-1.5-1.5-1.5h-1.5V13h1.5c.83 0 1.5-.67 1.5-1.5z"/>
    </svg>
  );
  
  const DataScienceIcon = () => (
    <svg className="w-10 h-10 mx-auto mb-2 text-green-600 dark:text-green-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
      <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z"/>
    </svg>
  );

  const EdgeMlIcon = () => (
    <svg className="w-10 h-10 mx-auto mb-2 text-red-600 dark:text-red-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
      <path d="M12 2c5.52 0 10 4.48 10 10s-4.48 10-10 10S2 17.52 2 12 6.48 2 12 2zm1 14h-2v-4H7V8h6c1.1 0 2 .9 2 2v4c0 1.1-.9 2-2 2zm-4.5-5.5h2v1h-2v-1z"/>
    </svg>
  );
  
  const CvIcon = () => (
    <svg className="w-10 h-10 mx-auto mb-2 text-purple-600 dark:text-purple-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
      <path d="M4 6h16v12H4V6zm16-2H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zM8 11.5c-.83 0-1.5.67-1.5 1.5s.67 1.5 1.5 1.5 1.5-.67 1.5-1.5-.67-1.5-1.5-1.5zm10 0c-.83 0-1.5.67-1.5 1.5s.67 1.5 1.5 1.5 1.5-.67 1.5-1.5-.67-1.5-1.5-1.5zM12 18c-3.31 0-6-2.69-6-6s2.69-6 6-6 6 2.69 6 6-2.69 6-6 6z"/>
    </svg>
  );

  const DataHandlingIcon = () => (
    <svg className="w-10 h-10 mx-auto mb-2 text-orange-600 dark:text-orange-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
      <path d="M21 17H3V5h18v12zm-3-4V9c0-.55-.45-1-1-1H7c-.55 0-1 .45-1 1v4c0 .55.45 1 1 1h10c.55 0 1-.45 1-1zm-6 3H7v-2h5v2zm4-4h-4V9h4v4z"/>
    </svg>
  );

  const GitIcon = () => (
    <svg className="w-10 h-10 mx-auto mb-2 text-gray-700 dark:text-gray-300" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
      <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.6.11 1.05-.259 1.05-.578v-1.996c-3.321.724-4.029-1.609-4.029-1.609-.54-1.368-1.32-1.734-1.32-1.734-1.082-.74.082-.725.082-.725 1.196.085 1.826 1.229 1.826 1.229 1.066 1.815 2.795 1.289 3.477.986.108-.767.419-1.289.762-1.589-2.652-.3-5.432-1.328-5.432-5.908 0-1.306.467-2.372 1.229-3.212-.124-.301-.535-1.52.124-3.179 0 0 1.006-.32 3.298 1.229 1.02-.283 2.091-.424 3.161-.424 2.292-1.549 3.298-1.229 3.298-1.229.659 1.659.248 2.878.124 3.179.762.84 1.229 1.906 1.229 3.212 0 4.591-2.78 5.601-5.432 5.908.431.376.819 1.115.819 2.247v3.314c0 .32.45.688 1.05.578C20.562 21.82 24 17.302 24 12 24 5.373 18.626 0 12 0z"/>
    </svg>
  );

  // --- Individual Sections ---

  const HeroSection = () => {
    const heroAnimationClass = 'animate-slide-up-fade';

    return (
      <section id="hero" className="pt-24 pb-16 md:pt-32 md:pb-24 bg-gray-50 dark:bg-gray-900 overflow-hidden relative transition-colors duration-500">
        <div className="container mx-auto px-6 lg:px-8 text-center max-w-4xl">
          <h1 className={`text-5xl sm:text-7xl font-extrabold text-gray-900 dark:text-gray-100 leading-tight mb-4 ${heroAnimationClass}`}>
            Hello, I'm <span className="text-blue-600 dark:text-blue-400">Kavya Dabhi</span>
          </h1>
          {/* New Typing Animation for job title */}
          <p className={`text-2xl sm:text-3xl text-gray-600 dark:text-gray-400 mb-6 ${heroAnimationClass} delay-[300ms]`}>
            <span className="typing-text font-mono text-blue-600 dark:text-blue-400 font-semibold inline-block">
              Machine Learning Engineer
            </span>
          </p>
          <p className={`text-lg sm:text-xl text-gray-600 dark:text-gray-400 mb-10 ${heroAnimationClass} delay-[600ms]`}>
            Motivated and results-oriented, specializing in Python and edge computing solutions.
          </p>
          <div className={`flex justify-center space-x-4 ${heroAnimationClass} delay-[900ms]`}>
            <a href="#projects" className="px-8 py-3 bg-blue-600 dark:bg-blue-700 text-white text-lg font-semibold rounded-full shadow-lg hover:bg-blue-700 dark:hover:bg-blue-600 transition duration-300 transform hover:scale-105">
              View ML Projects
            </a>
            <a href="#contact" className="px-8 py-3 border border-blue-600 dark:border-blue-400 text-blue-600 dark:text-blue-400 text-lg font-semibold rounded-full hover:bg-blue-600 hover:text-white dark:hover:bg-blue-400 dark:hover:text-gray-900 transition duration-300 transform hover:scale-105">
              Get In Touch
            </a>
          </div>
        </div>
        {/* Decorative Background Element with subtle pulsing animation */}
        <div className="absolute top-0 right-0 w-3/5 h-full bg-blue-200/50 dark:bg-blue-800/30 opacity-20 transform -skew-y-3 -translate-y-1/2 -translate-x-1/2 animate-pulse-slow"></div>
      </section>
    );
  };

  const AboutSection = () => {
    const [ref, inView] = useInView({ threshold: 0.3 });

    return (
      <section id="about" className="py-20 md:py-32 bg-white dark:bg-gray-800 overflow-hidden transition-colors duration-500">
        <div className="container mx-auto px-6 lg:px-8 max-w-6xl">
          <SectionHeader title="About Me" colorClass="text-blue-600 dark:text-blue-400" />
          <div ref={ref} className="md:flex md:space-x-12 items-center">
            {/* Image fades in and scales up */}
            <div className={`md:w-1/3 mb-8 md:mb-0 flex justify-center transition-all duration-1000 ease-out transform ${inView ? 'scale-100 opacity-100' : 'scale-75 opacity-0'}`}>
              {/* Placeholder photo updated for ML Engineer persona */}
              <img src="https://placehold.co/300x300/1e40af/ffffff?text=Kavya+Dabhi" alt="Professional Photo"
                   className="rounded-full w-48 h-48 sm:w-64 sm:h-64 object-cover shadow-2xl border-4 border-white dark:border-gray-700 ring-4 ring-blue-600/30 dark:ring-blue-400/30" />
            </div>
            {/* Text slides in from the right */}
            <div className={`md:w-2/3 text-xl text-gray-700 dark:text-gray-300 leading-relaxed transition-all duration-1000 ease-out delay-300 transform ${inView ? 'translate-x-0 opacity-100' : 'translate-x-10 opacity-0'}`}>
              <p className="mb-4">
                I am a motivated and results-oriented **Machine Learning Engineer** with 2+ years of experience leveraging **Python** and its powerful libraries to create solutions across diverse domains.
              </p>
              <p className="mb-4">
                My core competency lies in the full machine learning pipeline: from **strategic project management** and **data analysis** to building scalable models with **TensorFlow** and **Scikit-Learn**, and deploying impactful solutions.
              </p>
              <p>
                I am adept at collaborating in dynamic team environments, focusing on efficient data handling, feature engineering, and rigorous model evaluation to deliver innovative, end-to-end ML projects.
              </p>
            </div>
          </div>
        </div>
      </section>
    );
  };

  const EducationSection = () => {
    const [ref, inView] = useInView({ threshold: 0.2 });
    const education = [
      {
        degree: 'B.Tech in Electronics and Communication',
        institution: 'Charotar University of Science and Technology (CHARUSAT)',
        status: 'Completed 4th Semester',
        cert: 'Machine Learning Training (Acmegrade and Mood Indigo, IIT Bombay)',
        certDate: 'Sep - Oct 2023',
      },
    ];

    return (
      <section id="education" className="py-20 md:py-32 bg-gray-50 dark:bg-gray-900 overflow-hidden transition-colors duration-500">
        <div className="container mx-auto px-6 lg:px-8 max-w-6xl">
          <SectionHeader title="Education & Training" colorClass="text-blue-600 dark:text-blue-400" />
          <div ref={ref} className="grid md:grid-cols-1 gap-10">
            {education.map((item, index) => (
              <AnimatedCard key={index} delay={index * 200}>
                <div className="flex items-start space-x-6">
                  <div className="text-4xl text-blue-600 dark:text-blue-400 flex-shrink-0">
                    <svg className="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 21a9 9 0 009-9H3a9 9 0 009 9zM12 3c-4.418 0-8 3.582-8 8s3.582 8 8 8 8-3.582 8-8-3.582-8-8-8zM12 3v18"></path></svg>
                  </div>
                  <div>
                    <h3 className="text-2xl font-bold mb-1 text-gray-900 dark:text-gray-100">{item.degree}</h3>
                    <p className="text-lg text-blue-600 dark:text-blue-400 font-semibold mb-2">{item.institution}</p>
                    <p className="text-md text-gray-700 dark:text-gray-300 mb-4">Status: {item.status}</p>
                    <div className="bg-gray-100 dark:bg-gray-700 p-4 rounded-lg border-l-4 border-blue-500">
                      <p className="font-medium text-gray-800 dark:text-gray-200">{item.cert}</p>
                      <p className="text-sm text-gray-500 dark:text-gray-400 mt-1">Completion Date: {item.certDate}</p>
                    </div>
                  </div>
                </div>
              </AnimatedCard>
            ))}
          </div>
        </div>
      </section>
    );
  };

  const SkillsSection = () => {
    // Reusing the MlIcon definition for all skills
    const skills = [
      { name: 'Python (Advanced)', detail: 'TensorFlow, Scikit-Learn', icon: <PythonIcon /> },
      { name: 'Data Science Stack', detail: 'Pandas, NumPy, Matplotlib, Seaborn', icon: <DataScienceIcon /> },
      { name: 'Edge ML / Micro-Python', detail: 'ESP32, Real-time Anomaly Detection', icon: <EdgeMlIcon /> },
      { name: 'Computer Vision', detail: 'OpenCV, Face Detection', icon: <CvIcon /> },
      { name: 'Data Handling', detail: 'Preprocessing, Feature Engineering, MySQL', icon: <DataHandlingIcon /> },
      { name: 'Version Control', detail: 'Git & GitHub Workflow', icon: <GitIcon /> },
    ];

    return (
      <section id="skills" className="py-20 md:py-32 bg-white dark:bg-gray-800 overflow-hidden transition-colors duration-500">
        <div className="container mx-auto px-6 lg:px-8 max-w-6xl text-center">
          <SectionHeader title="Technical Skillset" colorClass="text-blue-600 dark:text-blue-400" />
          <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-6">
            {skills.map((skill, index) => (
              <AnimatedCard key={skill.name} delay={index * 150}>
                <div className="flex flex-col items-center">
                  {skill.icon}
                  <p className="text-lg font-semibold text-gray-800 dark:text-gray-200">{skill.name}</p>
                  <div className="text-xs text-gray-500 dark:text-gray-400 mt-1">{skill.detail}</div>
                </div>
              </AnimatedCard>
            ))}
          </div>
        </div>
      </section>
    );
  };

  const ProjectsSection = () => {
    // All projects from the resume are now included
    const projects = [
      {
        id: 1,
        title: 'ML on Edge: Environmental Monitoring System',
        tech: ['Micro-Python', 'Edge ML', 'ESP32'],
        desc: 'Developed a real-time system using ESP32, Micro-Python, and Edge ML for anomaly detection on sensor data (DHT22, MQ135) for temperature, humidity, and air quality.',
        link: 'https://github.com/MoMstealer05/Environmental-Monitoring-System'
      },
      {
        id: 2,
        title: 'Stock Price Prediction System',
        tech: ['Python', 'ML Models', 'Pandas'],
        desc: 'Implemented time-series ML models for stock price forecasting, focusing on data preprocessing, feature engineering, and rigorous evaluation for high accuracy.',
        link: 'https://github.com/MoMstealer05' // Placeholder link for project repo
      },
      {
        id: 3,
        title: 'Cancer Prediction Model',
        tech: ['Scikit-Learn', 'Data Analysis', 'Python'],
        desc: 'Developed a robust ML classification model for critical medical prediction tasks, assessing cancer risk based on historical patient data.',
        link: 'https://github.com/MoMstealer05' // Placeholder link for project repo
      },
      {
        id: 4,
        title: 'Home Security System with Telegram Notifications',
        tech: ['ESP32', 'Telegram API', 'IoT'],
        desc: 'Created a security system using ESP32 to monitor conditions and trigger real-time alerts and security notifications via the Telegram API.',
        link: 'https://github.com/MoMstealer05' // Placeholder link for project repo
      },
      {
        id: 5,
        title: 'Movies Recommendation System',
        tech: ['Python', 'Collaborative Filtering', 'Pandas'],
        desc: 'Built a recommendation engine using collaborative filtering techniques to provide personalized movie suggestions based on user preference and history.',
        link: 'https://github.com/MoMstealer05' // Placeholder link for project repo
      },
      {
        id: 6,
        title: 'GPS Locator',
        tech: ['ESP32', 'NEO-6M GPS', 'IoT'],
        desc: 'Designed a real-time GPS tracking solution using ESP32 and NEO-6M module for location uploads and monitoring.',
        link: 'https://github.com/MoMstealer05' // Placeholder link for project repo
      },
      {
        id: 7,
        title: 'Face Detection (Real-time)',
        tech: ['OpenCV', 'Python', 'Computer Vision'],
        desc: 'Developed a real-time face detection application using OpenCV for foundational computer vision tasks and analysis.',
        link: 'https://github.com/MoMstealer05' // Placeholder link for project repo
      },
      {
        id: 8,
        title: 'Music Recommendation System',
        tech: ['Python', 'ML', 'User Preferences'],
        desc: 'Implemented a system for song suggestions by analyzing and modeling user preferences and listening patterns.',
        link: 'https://github.com/MoMstealer05' // Placeholder link for project repo
      },
    ];

    return (
      <section id="projects" className="py-20 md:py-32 bg-gray-50 dark:bg-gray-900 overflow-hidden transition-colors duration-500">
        <div className="container mx-auto px-6 lg:px-8 max-w-6xl">
          <SectionHeader title="Showcase of ML Work" colorClass="text-blue-600 dark:text-blue-400" />
          {/* Change grid to 3 columns for better display of 8 projects */}
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-10">
            {projects.map((project, index) => (
              <AnimatedCard key={project.id} delay={index * 100}> {/* Reduced delay for smoother load */}
                <h3 className="text-2xl font-bold mb-2 text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300 transition">{project.title}</h3>
                <p className="text-gray-600 dark:text-gray-300 mb-4 text-sm">{project.desc}</p>
                <div className="flex flex-wrap gap-2 mb-4">
                  {project.tech.map(t => (
                    <span key={t} className="bg-blue-100 dark:bg-blue-900 text-blue-600 dark:text-blue-300 text-xs font-medium px-3 py-1 rounded-full border border-blue-200 dark:border-blue-700">{t}</span>
                  ))}
                </div>
                <a href={project.link} target="_blank" rel="noopener noreferrer" className="inline-flex items-center text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300 font-semibold transition duration-300 group">
                  View Source
                  <svg className="w-5 h-5 ml-1 transition-transform duration-300 group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                </a>
              </AnimatedCard>
            ))}
          </div>
          <div className="text-center mt-12">
            <a href="https://github.com/MoMstealer05" target="_blank" rel="noopener noreferrer" className="px-8 py-3 bg-blue-600 dark:bg-blue-700 text-white text-lg font-semibold rounded-full shadow-lg hover:bg-blue-700 dark:hover:bg-blue-600 transition duration-300 transform hover:scale-105">
                See All on GitHub
            </a>
          </div>
        </div>
      </section>
    );
  };

  const ContactSection = () => {
    const [ref, inView] = useInView({ threshold: 0.2 });

    return (
      <section id="contact" className="py-20 md:py-32 bg-white dark:bg-gray-800 overflow-hidden transition-colors duration-500">
        <div className="container mx-auto px-6 lg:px-8 max-w-xl">
          <SectionHeader title="Let's Connect" colorClass="text-blue-600 dark:text-blue-400" />
          <p className="text-xl text-gray-700 dark:text-gray-300 mb-8 text-center">
            I'm always looking for innovative teams and challenging projects. Reach out via email, phone, or the form below!
          </p>

          {/* Contact Details Block - Updated with explicit email */}
          <div className="flex justify-center space-x-6 mb-8 text-lg font-medium text-gray-700 dark:text-gray-300">
            <a href="mailto:dabhikavya189@gmail.com" className="hover:text-blue-600 dark:hover:text-blue-400 transition flex items-center">
              <svg className="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"></path></svg>
              dabhikavya189@gmail.com
            </a>
            <a href="tel:+919313713692" className="hover:text-blue-600 dark:hover:text-blue-400 transition flex items-center">
              <svg className="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.89 5.28 6.72 6.72l2.42-2.42c.28-.28.67-.36 1.02-.23 1.09.34 2.13.52 3.22.52.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.09.18 2.13.52 3.22.13.35.05.74-.23 1.02l-2.42 2.42z"></path></svg>
              +91 93137 13692
            </a>
          </div>

          {/* Contact Form with animation */}
          <form ref={ref} className={`space-y-6 bg-gray-50 dark:bg-gray-900 p-8 rounded-xl shadow-2xl transition-all duration-1000 ease-out transform ${inView ? 'translate-y-0 opacity-100' : 'translate-y-10 opacity-0'}`}>
              <div>
                  <label htmlFor="name" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Name</label>
                  <input type="text" id="name" name="name" required
                         className="w-full px-4 py-3 border border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-gray-100 rounded-lg focus:ring-blue-600 dark:focus:ring-blue-400 focus:border-blue-600 dark:focus:border-blue-400 transition duration-300" />
              </div>
              <div>
                  <label htmlFor="email" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Email</label>
                  <input type="email" id="email" name="email" required
                         className="w-full px-4 py-3 border border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-gray-100 rounded-lg focus:ring-blue-600 dark:focus:ring-blue-400 focus:border-blue-600 dark:focus:border-blue-400 transition duration-300" />
              </div>
              <div>
                  <label htmlFor="message" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Message</label>
                  <textarea id="message" name="message" rows="5" required
                            className="w-full px-4 py-3 border border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-gray-100 rounded-lg focus:ring-blue-600 dark:focus:ring-blue-400 focus:border-blue-600 dark:focus:border-blue-400 transition duration-300"></textarea>
              </div>
              <div>
                  <button type="submit"
                          className="w-full px-6 py-3 bg-blue-600 dark:bg-blue-700 text-white text-xl font-semibold rounded-full shadow-lg hover:bg-blue-700 dark:hover:bg-blue-600 transition duration-300 transform hover:scale-[1.01]">
                      Send Secure Message
                  </button>
              </div>
          </form>

          <div className="mt-12 text-center text-gray-600 dark:text-gray-400 space-y-2">
              <p>Find me on social media:</p>
              <div className="flex justify-center space-x-6 mt-4">
                {/* LinkedIn Icon */}
                <a href="https://www.linkedin.com/in/kavya-dabhi-69632a265/" target="_blank" rel="noopener noreferrer" className="text-gray-500 dark:text-gray-400 hover:text-blue-600 dark:hover:text-blue-400 transition duration-300 transform hover:scale-125">
                    <svg className="w-8 h-8" fill="currentColor" viewBox="0 0 24 24"><path d="M4.98 3.5c0 1.381-1.11 2.5-2.48 2.5s-2.48-1.119-2.48-2.5c0-1.38 1.11-2.5 2.48-2.5s2.48 1.12 2.48 2.5zm.02 4.5h-5v16h5v-16zm7.98 0h-7.98v16h7.98v-16zm-7.98 0h-5v16h5v-16zm7.98 0h-7.98v16h7.98v-16zM15 15h-3v-2.5c0-.96.04-1.63 1.25-1.63C14.47 10.87 15 11.75 15 13.06V15h3v-4.5c0-1.92-1.09-3.41-3.03-3.41-1.4 0-1.89.75-2.26 1.48h-.06v-1.29H7v16h3v-5.25c0-1.25.06-2.46.75-3.32.74-.95 1.94-1.57 3.32-1.57 2.37 0 3.38 1.76 3.38 4.29V15h3v-5.25c0-1.92-1.09-3.41-3.03-3.41-1.4 0-1.89.75-2.26 1.48h-.06v-1.29H7v16h3v-5.25c0-1.25.06-2.46.75-3.32.74-.95 1.94-1.57 3.32-1.57 2.37 0 3.38 1.76 3.38 4.29V15z"/></svg>
                </a>
                {/* GitHub Icon */}
                <a href="https://github.com/MoMstealer05" target="_blank" rel="noopener noreferrer" className="text-gray-500 dark:text-gray-400 hover:text-blue-600 dark:hover:text-blue-400 transition duration-300 transform hover:scale-125">
                    <svg className="w-8 h-8" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.6.11 1.05-.259 1.05-.578v-1.996c-3.321.724-4.029-1.609-4.029-1.609-.54-1.368-1.32-1.734-1.32-1.734-1.082-.74.082-.725.082-.725 1.196.085 1.826 1.229 1.826 1.229 1.066 1.815 2.795 1.289 3.477.986.108-.767.419-1.289.762-1.589-2.652-.3-5.432-1.328-5.432-5.908 0-1.306.467-2.372 1.229-3.212-.124-.301-.535-1.52.124-3.179 0 0 1.006-.32 3.298 1.229 1.02-.283 2.091-.424 3.161-.424 2.292-1.549 3.298-1.229 3.298-1.229.659 1.659.248 2.878.124 3.179.762.84 1.229 1.906 1.229 3.212 0 4.591-2.78 5.601-5.432 5.908.431.376.819 1.115.819 2.247v3.314c0 .32.45.688 1.05.578C20.562 21.82 24 17.302 24 12 24 5.373 18.626 0 12 0z"/></svg>
                </a>
              </div>
          </div>
        </div>
      </section>
    );
  };

  return (
    // Main container uses dark classes to set the default background and text colors
    <div className="font-sans text-gray-800 bg-gray-100 min-h-screen dark:bg-gray-900 dark:text-gray-200 transition-colors duration-500">
      {/* This style block contains the custom CSS animations and Tailwind configuration. */}
      <style>{`
        /* 1. Keyframe for Hero Text Entry (Slide Up and Fade In) */
        @keyframes slide-up-fade {
          0% {
            opacity: 0;
            transform: translateY(20px);
          }
          100% {
            opacity: 1;
            transform: translateY(0);
          }
        }
        .animate-slide-up-fade {
          animation: slide-up-fade 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
          opacity: 0; /* Initial state before animation */
        }
        /* Delay utility classes for staggering the hero text */
        .delay-\\[300ms\\] { animation-delay: 300ms; }
        .delay-\\[600ms\\] { animation-delay: 600ms; }
        .delay-\\[900ms\\] { animation-delay: 900ms; }
        
        /* 2. Background Pulse Animation */
        @keyframes pulse-slow {
          0%, 100% { opacity: 0.2; }
          50% { opacity: 0.35; }
        }
        .animate-pulse-slow {
          animation: pulse-slow 15s infinite ease-in-out;
        }

        /* 3. Global transitions for smoother hovers/focus */
        .transition-all {
            transition-property: all;
            transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        /* 4. Typing Effect for Job Title */
        .typing-text {
          overflow: hidden; /* Ensures the content is not revealed until the animation */
          border-right: .15em solid #3b82f6; /* The caret/cursor (blue) */
          white-space: nowrap; /* Keeps the content on a single line */
          margin: 0 auto; /* Gives that typewriter effect */
          letter-spacing: .05em; /* Adjust as needed */
          animation:
            typing 1.5s steps(27, end) forwards, /* 27 characters in 'Machine Learning Engineer' */
            blink-caret .75s step-end infinite;
          width: 0; /* Starts at zero width */
          display: inline-block;
          animation-fill-mode: forwards;
        }
        .dark .typing-text {
            border-right-color: #60a5fa; /* Lighter blue for dark mode cursor */
        }
        @keyframes typing {
          from { width: 0 }
          to { width: 100% }
        }
        @keyframes blink-caret {
          from, to { border-color: transparent }
          50% { border-color: inherit } /* Inherits the text color for contrast */
        }

      `}</style>

      {/* Sticky Navigation */}
      <header className="sticky top-0 z-50 bg-white/90 dark:bg-gray-900/90 backdrop-blur-md shadow-lg dark:shadow-blue-800/20 transition duration-500">
        <nav className="container mx-auto px-4 sm:px-6 lg:px-8 py-4 flex justify-between items-center">
          {/* LOGO: Kavya Dabhi */}
          <a href="#" className="text-3xl font-extrabold text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300 transition transform hover:scale-105">Kavya Dabhi</a>
          <div className="flex space-x-4 md:space-x-8 items-center">
            <a href="#about" className="text-gray-600 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 transition font-medium text-lg">About</a>
            <a href="#skills" className="text-gray-600 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 transition font-medium text-lg">Skills</a>
            <a href="#education" className="text-gray-600 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 transition font-medium text-lg">Education</a>
            <a href="#projects" className="text-gray-600 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 transition font-medium text-lg">Projects</a>
            <a href="#contact" className="text-gray-600 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 transition font-medium text-lg">Contact</a>
            {/* Dark Mode Toggle */}
            <DarkModeToggle darkMode={darkMode} setDarkMode={setDarkMode} />
          </div>
        </nav>
      </header>

      <main>
        <HeroSection />
        <AboutSection />
        <SkillsSection />
        <EducationSection />
        <ProjectsSection />
        <ContactSection />
      </main>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-8 transition-colors duration-500">
        <div className="container mx-auto px-6 lg:px-8 text-center">
          <p className="text-lg font-light">&copy; {new Date().getFullYear()} Kavya Dabhi. All rights reserved.</p>
          {/* UPDATED FOOTER TEXT */}
          <p className="text-sm mt-2 text-gray-400">Intelligent Systems Portfolio built with Machine Learning & Edge Computing.</p>
        </div>
      </footer>
    </div>
  );
};

export default App;
