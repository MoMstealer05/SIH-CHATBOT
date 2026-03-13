import os
import json

# This list contains all 37 of your intents and their complete training phrases
# in the format that you confirmed works with your Dialogflow agent.
INTENT_DATA = [
    {"intentName": "ask_about_scholarships", "trainingPhrases": {
        "en": ["Are there any scholarships available?", "How can I apply for a scholarship?", "What are the eligibility criteria for scholarships?", "Tell me about financial aid options.", "I need information on student grants.", "Where can I find the scholarship application form?", "What is the deadline for scholarship applications?", "Are there merit-based scholarships?", "Can you list the available scholarships?", "I want to know more about the scholarship program.", "koi scholarship available hai?", "scholarship ke liye kaise apply karu?", "scholarship eligibility criteria kya hai?", "financial aid options ke bare me batao.", "koi scholarship chhe?", "scholarship mate kevi rite apply karvanu?", "scholarship mate eligibility shu chhe?", "mane financial aid options vishe janavo."],
        "hi": ["कोई छात्रवृत्ति उपलब्ध है?", "मैं छात्रवृत्ति के लिए आवेदन कैसे कर सकता हूं?", "छात्रवृत्ति के लिए पात्रता मानदंड क्या हैं?", "वित्तीय सहायता विकल्पों के बारे में बताएं।"],
        "gu": ["શું કોઈ શિષ્યવૃત્તિ ઉપલબ્ધ છે?", "હું શિષ્યવૃત્તિ માટે કેવી રીતે અરજી કરી શકું?", "શિષ્યવૃત્તિ માટે પાત્રતા માપદંડ શું છે?", "મને નાણાકીય સહાયના વિકલ્પો વિશે કહો."]
    }},
    {"intentName": "ask_academic_council_role", "trainingPhrases": {
        "en": ["What does the academic council do?", "What is the role of the academic council?", "Who is on the academic council?", "What are the responsibilities of the academic council?", "Tell me about the function of the academic council.", "academic council kya karti hai?", "academic council ka role kya hai?", "academic council ki responsibilities kya hain?", "academic council shu kaam kare chhe?", "academic council no role shu chhe?", "academic council ni javabdari shu chhe?"],
        "hi": ["अकादमिक परिषद क्या करती है?", "अकादमिक परिषद की क्या भूमिका है?", "अकादमिक परिषद की जिम्मेदारियां क्या हैं?"],
        "gu": ["શૈક્ષણિક પરિષદ શું કરે છે?", "શૈક્ષણિક પરિષદની ભૂમિકા શું છે?", "શૈક્ષણિક પરિષદની જવાબદારીઓ શું છે?"]
    }},
    {"intentName": "ask_academic_misconduct_policy", "trainingPhrases": {
        "en": ["What is the policy on cheating?", "What happens if a student is caught plagiarizing?", "Tell me about the academic misconduct policy.", "What are the consequences of academic dishonesty?", "I need to understand the rules about plagiarism.", "Where can I find the academic integrity policy?", "What constitutes academic misconduct?", "cheating par kya policy hai?", "plagiarism karte pakde gaye to kya hota hai?", "academic misconduct policy ke bare me batao.", "cheating ange shu policy chhe?", "jo koi student sahityachori karta pakday to shu thay?", "mane academic misconduct policy vishe janavo."],
        "hi": ["नकल करने पर क्या नीति है?", "यदि कोई छात्र साहित्यिक चोरी करते हुए पकड़ा जाता है तो क्या होता है?", "शैक्षणिक कदाचार नीति के बारे में बताएं।"],
        "gu": ["ચિટિંગ અંગેની નીતિ શું છે?", "જો કોઈ વિદ્યાર્થી સાહિત્યચોરી કરતા પકડાય તો શું થાય?", "મને શૈક્ષણિક ગેરરીતિની નીતિ વિશે કહો."]
    }},
    {"intentName": "ask_admission_process", "trainingPhrases": {
        "en": ["How do I apply for admission?", "What is the admission process?", "What are the steps for getting admission here?", "Tell me about the application procedure.", "What documents are required for admission?", "admission ke liye kaise apply karu?", "admission process kya hai?", "admission ke liye kya documents chahiye?", "admission mate kevi rite apply karvanu?", "admission process shu chhe?", "admission mate kaya documents joiye?"],
        "hi": ["मैं प्रवेश के लिए आवेदन कैसे करूं?", "प्रवेश प्रक्रिया क्या है?", "प्रवेश के लिए कौन से दस्तावेज़ आवश्यक हैं?"],
        "gu": ["હું પ્રવેશ માટે કેવી રીતે અરજી કરી શકું?", "પ્રવેશ પ્રક્રિયા શું છે?", "પ્રવેશ માટે કયા દસ્તાવેજો જરૂરી છે?"]
    }},
    {"intentName": "ask_admission_refund_policy", "trainingPhrases": {
        "en": ["What is the admission fee refund policy?", "If I cancel my admission, will I get a refund?", "Tell me about the refund rules for admission fees.", "How much money will be refunded if I withdraw my application?", "Can I get a full refund of my admission fee?", "admission fee refund policy kya hai?", "agar admission cancel karu to refund milega?", "full admission fee refund mil sakti hai?", "admission fee refund policy shu chhe?", "jo admission cancel karavu to refund malishe?", "mane full admission fee refund mali shake?"],
        "hi": ["प्रवेश शुल्क वापसी नीति क्या है?", "यदि मैं अपना प्रवेश रद्द करता हूं, तो क्या मुझे धनवापसी मिलेगी?", "क्या मुझे अपनी प्रवेश शुल्क की पूरी वापसी मिल सकती है?"],
        "gu": ["પ્રવેશ ફી રિફંડ નીતિ શું છે?", "જો હું મારો પ્રવેશ રદ કરું, તો શું મને રિફંડ મળશે?", "શું મને મારી પ્રવેશ ફીનું સંપૂર્ણ રિફંડ મળી શકે છે?"]
    }},
    {"intentName": "ask_available_programs", "trainingPhrases": {
        "en": ["What courses do you offer?", "What programs are available at this college?", "Can you list the different departments?", "I want to know about the engineering branches available.", "Do you have a computer science program?", "aap kaun se course offer karte hain?", "is college me kon se programs available hai?", "kya computer science program hai?", "tame kaya abhyaskram offer karo chho?", "aa college ma kaya program available chhe?", "shu tamari pase computer science program chhe?"],
        "hi": ["आप कौन से पाठ्यक्रम प्रदान करते हैं?", "इस कॉलेज में कौन से कार्यक्रम उपलब्ध हैं?", "क्या आपके पास कंप्यूटर विज्ञान कार्यक्रम है?"],
        "gu": ["તમે કયા અભ્યાસક્રમો ઓફર કરો છો?", "આ કોલેજમાં કયા પ્રોગ્રામ ઉપલબ્ધ છે?", "શું તમારી પાસે કમ્પ્યુટર સાયન્સ પ્રોગ્રામ છે?"]
    }},
    {"intentName": "ask_btech_max_completion_time", "trainingPhrases": {
        "en": ["How long does it take to complete the B.Tech course?", "What is the maximum time allowed to complete my B.Tech degree?", "What is the duration of the B.Tech program?", "Is there a time limit for finishing the B.Tech program?", "How many years do I have to complete my graduation in B.Tech?", "B.Tech course complete karne me kitna time lagta hai?", "B.Tech degree complete karne ka max time kya hai?", "B.Tech course puro karva ma ketlo time lage chhe?", "B.Tech degree puri karva mate maximum time keto chhe?"],
        "hi": ["बी.टेक कोर्स पूरा करने में कितना समय लगता है?", "मेरी बी.टेक डिग्री पूरी करने के लिए अधिकतम कितना समय दिया गया है?"],
        "gu": ["બી.ટેક. કોર્સ પૂરો કરવામાં કેટલો સમય લાગે છે?", "મારી બી.ટેક. ડિગ્રી પૂરી કરવા માટે મહત્તમ કેટલો સમય આપવામાં આવે છે?"]
    }},
    {"intentName": "ask_course_completion_time", "trainingPhrases": {
        "en": ["How long does it take to complete the B.E. course?", "What is the maximum time allowed to complete my degree?", "What is the duration of the engineering program?", "Is there a time limit for finishing the M.E. program?", "How many years do I have to complete my graduation?", "BE course complete karne me kitna time lagta hai?", "degree complete karne ka max time kya hai?", "BE course puro karva ma ketlo time lage chhe?", "degree puri karva mate maximum time keto chhe?"],
        "hi": ["बी.ई. कोर्स पूरा करने में कितना समय लगता है?", "मेरी डिग्री पूरी करने के लिए अधिकतम कितना समय दिया गया है?"],
        "gu": ["બી.ઈ. કોર્સ પૂરો કરવામાં કેટલો સમય લાગે છે?", "મારી ડિગ્રી પૂરી કરવા માટે મહત્તમ કેટલો સમય આપવામાં આવે છે?"]
    }},
    {"intentName": "ask_contact_details", "trainingPhrases": {
        "en": ["How can I contact the college?", "What is the college's phone number?", "What is the official email address?", "I need the contact details for the administration office.", "Can you give me the address of the college?", "college se kaise contact karu?", "college ka phone number kya hai?", "official email address kya hai?", "college no sampark kevi rite karu?", "college no phone number shu chhe?", "official email address shu chhe?"],
        "hi": ["मैं कॉलेज से कैसे संपर्क कर सकता हूं?", "कॉलेज का फोन नंबर क्या है?", "आधिकारिक ईमेल पता क्या है?"],
        "gu": ["હું કોલેજનો સંપર્ક કેવી રીતે કરી શકું?", "કોલેજનો ફોન નંબર શું છે?", "સત્તાવાર ઇમેઇલ સરનામું શું છે?"]
    }},
    {"intentName": "ask_cspt_phone", "trainingPhrases": {
        "en": ["What is the phone number for the CSPIT?", "How can I call the CSPIT office?", "I need the contact number for the Chandubhai S Patel Institute of Technology.", "CSPIT ka phone number kya hai?", "CSPIT office me kaise call karu?", "CSPIT no phone number shu chhe?", "CSPIT office ma kevi rite phone karu?"],
        "hi": ["CSPIT का फ़ोन नंबर क्या है?", "मैं CSPIT कार्यालय में कैसे कॉल कर सकता हूं?"],
        "gu": ["CSPIT નો ફોન નંબર શું છે?", "હું CSPIT ઓફિસમાં કેવી રીતે ફોન કરી શકું?"]
    }},
    {"intentName": "ask_cspt_principal_email", "trainingPhrases": {
        "en": ["What is the email address of the CSPIT principal?", "How can I email the principal of CSPIT?", "I need the principal's official email ID.", "CSPIT principal ka email address kya hai?", "CSPIT principal ko kaise email karu?", "CSPIT na principal nu email address shu chhe?", "CSPIT na principal ne kevi rite email karu?"],
        "hi": ["CSPIT के प्रिंसिपल का ईमेल पता क्या है?", "मैं CSPIT के प्रिंसिपल को कैसे ईमेल कर सकता हूं?"],
        "gu": ["CSPIT ના પ્રિન્સિપાલનું ઇમેઇલ સરનામું શું છે?", "હું CSPIT ના પ્રિન્સિપાલને કેવી રીતે ઇમેઇલ કરી શકું?"]
    }},
    {"intentName": "ask_education_system", "trainingPhrases": {
        "en": ["What education system does the college follow?", "Is it a semester-based system?", "Tell me about the academic structure.", "How does the credit system work?", "Is the curriculum based on CBCS?", "college kon sa education system follow karta hai?", "semester based system hai kya?", "credit system kaise kaam karta hai?", "college kai shikshan pranali ne anusare chhe?", "shu te semester-based system chhe?", "credit system kevi rite kaam kare chhe?"],
        "hi": ["कॉलेज किस शिक्षा प्रणाली का पालन करता है?", "क्या यह सेमेस्टर आधारित प्रणाली है?", "क्रेडिट सिस्टम कैसे काम करता है?"],
        "gu": ["કોલેજ કઈ શિક્ષણ પ્રણાલીને અનુસરે છે?", "શું તે સેમેસ્ટર-આધારિત સિસ્ટમ છે?", "ક્રેડિટ સિસ્ટમ કેવી રીતે કાર્ય કરે છે?"]
    }},
    {"intentName": "ask_eligibility_criteria", "trainingPhrases": {
        "en": ["What are the eligibility criteria for admission?", "Who is eligible to apply for the B.E. program?", "What are the minimum requirements for the M.E. course?", "Am I eligible for admission?", "What percentage is required for computer engineering?", "admission ke liye eligibility criteria kya hai?", "BE program ke liye kon eligible hai?", "computer engineering ke liye kitna percentage chahiye?", "admission mate eligibility criteria shu chhe?", "BE program mate kon patra chhe?", "computer engineering mate ketla taka joiye?"],
        "hi": ["प्रवेश के लिए पात्रता मानदंड क्या हैं?", "बी.ई. कार्यक्रम के लिए कौन पात्र है?", "कंप्यूटर इंजीनियरिंग के लिए कितने प्रतिशत की आवश्यकता है?"],
        "gu": ["પ્રવેશ માટે પાત્રતા માપદંડ શું છે?", "બી.ઈ. પ્રોગ્રામ માટે કોણ પાત્ર છે?", "કમ્પ્યુટર એન્જિનિયરિંગ માટે કેટલા ટકા જરૂરી છે?"]
    }},
    {"intentName": "ask_fee_deadline", "trainingPhrases": {
        "en": ["When is the fee deadline?", "What is the last date to pay fees?", "When are the college fees due?", "Tell me the fee payment deadline.", "How long do I have to pay my tuition?", "What is the last day for fee submission?", "I need to know the deadline for semester fees.", "Can I pay my fees after the due date?", "Is there a late fee for payment?", "fees kab tak bharni hai?", "fees ki last date kya hai?", "college fees kab due hai?", "semester fees ki deadline kya hai?", "late fee lagegi kya?", "fees bharvani chhelli tarikh kyare chhe?", "college ni fees kyare due chhe?", "semester fees ni deadline shu chhe?", "late fee lagishe?"],
        "hi": ["फीस की अंतिम तिथि क्या है?", "फीस कब तक भरनी है?", "कॉलेज की फीस कब देय है?", "सेमेस्टर फीस की अंतिम तिथि क्या है?"],
        "gu": ["ફી ભરવાની છેલ્લી તારીખ ક્યારે છે?", "કોલેજની ફી ક્યારે ભરવાની છે?", "સેમેસ્ટર ફી માટેની છેલ્લી તારીખ શું છે?", "શું નિયત તારીખ પછી ફી ભરી શકાય?"]
    }},
    {"intentName": "ask_financial_aid_for_conferences", "trainingPhrases": {
        "en": ["Does the college provide financial aid for attending conferences?", "Is there funding for students to go to technical events?", "How can I get sponsorship for a conference?", "kya college conferences attend karne ke liye financial aid deta hai?", "shu college conference ma bhag leva mate financial sahay pure pade chhe?"],
        "hi": ["क्या कॉलेज सम्मेलनों में भाग लेने के लिए वित्तीय सहायता प्रदान करता है?"],
        "gu": ["શું કોલેજ કોન્ફરન્સમાં ભાગ લેવા માટે નાણાકીય સહાય પૂરી પાડે છે?"]
    }},
    {"intentName": "ask_hostel_facility", "trainingPhrases": {
        "en": ["Is there a hostel facility available?", "Tell me about the college accommodation.", "How are the hostel rooms?", "What are the hostel charges?", "Is the mess facility included with the hostel?", "How do I apply for the hostel?", "Are the hostels separate for boys and girls?", "hostel facility available hai?", "college accommodation ke bare me batao.", "hostel charges kya hain?", "mess facility included hai kya?", "hostel facility chhe?", "college na accommodation vishe janavo.", "hostel no charge shu chhe?", "mess ni suvidha chhe hostel ma?"],
        "hi": ["क्या छात्रावास की सुविधा उपलब्ध है?", "कॉलेज आवास के बारे में बताएं।", "छात्रावास का शुल्क क्या है?", "क्या छात्रावास में मेस की सुविधा शामिल है?"],
        "gu": ["શું છાત્રાલયની સુવિધા ઉપલબ્ધ છે?", "કોલેજના આવાસ વિશે મને કહો.", "છાત્રાલયનો ચાર્જ શું છે?", "શું છાત્રાલયમાં મેસની સુવિધા શામેલ છે?"]
    }},
    {"intentName": "ask_how_to_file_grievance", "trainingPhrases": {
        "en": ["How do I file a grievance?", "What is the procedure for submitting a complaint?", "Who should I contact to report an issue?", "Is there a student grievance cell?", "I want to file a formal complaint.", "grievance kaise file karu?", "complaint submit karne ka procedure kya hai?", "student grievance cell hai kya?", "fariyad kevi rite dakhal karu?", "fariyad dakhal karvani prakriya shu chhe?", "shu vidyarthi fariyad nivaran cell chhe?"],
        "hi": ["मैं शिकायत कैसे दर्ज करूं?", "शिकायत प्रस्तुत करने की प्रक्रिया क्या है?", "एक छात्र शिकायत प्रकोष्ठ है?"],
        "gu": ["હું ફરિયાદ કેવી રીતે દાખલ કરી શકું?", "ફરિયાદ દાખલ કરવાની પ્રક્રિયા શું છે?", "શું વિદ્યાર્થી ફરિયાદ નિવારણ સેલ છે?"]
    }},
    {"intentName": "ask_how_to_get_library_card", "trainingPhrases": {
        "en": ["How do I get a library card?", "What is the process for getting a library membership?", "Where do I apply for a library card?", "What documents are needed for a library card?", "I lost my library card, how to get a new one?", "library card kaise milega?", "library membership ke liye kya process hai?", "library card ke liye kya documents chahiye?", "library card kevi rite kadhavanu?", "library membership mate shu process chhe?", "library card mate kaya documents joiye?"],
        "hi": ["मुझे लाइब्रेरी कार्ड कैसे मिलेगा?", "लाइब्रेरी सदस्यता प्राप्त करने की प्रक्रिया क्या है?", "लाइब्रेरी कार्ड के लिए कौन से दस्तावेज़ चाहिए?"],
        "gu": ["મારે લાઇબ્રેરી કાર્ડ કેવી રીતે મેળવવું?", "લાઇબ્રેરી સભ્યપદ મેળવવાની પ્રક્રિયા શું છે?", "લાઇબ્રેરી કાર્ડ માટે કયા દસ્તાવેજોની જરૂર છે?"]
    }},
    {"intentName": "ask_how_to_pay_fees", "trainingPhrases": {
        "en": ["How can I pay my college fees?", "What are the different payment methods for fees?", "Can I pay my fees online?", "Where is the cash counter for fee payment?", "What is the link for the payment portal?", "college fees kaise pay kar sakta hu?", "fees pay karne ke kya methods hai?", "online fees pay kar sakte hai?", "college ni fees kevi rite bharvanu?", "fees bharvana alag alag method kaya chhe?", "online fees bhari shakay?"],
        "hi": ["मैं अपनी कॉलेज की फीस कैसे भर सकता हूं?", "शुल्क के लिए विभिन्न भुगतान विधियां क्या हैं?", "क्या मैं अपनी फीस ऑनलाइन भर सकता हूं?"],
        "gu": ["હું મારી કોલેજની ફી કેવી રીતે ભરી શકું?", "ફી માટે વિવિધ ચુકવણી પદ્ધતિઓ કઈ છે?", "શું હું મારી ફી ઓનલાઈન ભરી શકું?"]
    }},
    {"intentName": "ask_library_timings", "trainingPhrases": {
        "en": ["What are the library timings?", "When does the library open?", "What time does the library close?", "Is the library open on weekends?", "Can you tell me the library's working hours?", "Library timings during exams?", "library timings kya hai?", "library kab khulti hai?", "library weekends pe open rehti hai?", "library no time shu chhe?", "library kyare khule chhe?", "library weekends ma khulli hoy chhe?"],
        "hi": ["पुस्तकालय का समय क्या है?", "पुस्तकालय कब खुलता है?", "क्या पुस्तकालय सप्ताहांत पर खुला रहता है?"],
        "gu": ["લાઇબ્રેરીનો સમય શું છે?", "લાઇબ્રેરી ક્યારે ખુલે છે?", "શું લાઇબ્રેરી સપ્તાહના અંતે ખુલ્લી રહે છે?"]
    }},
    {"intentName": "ask_minimum_attendance", "trainingPhrases": {
        "en": ["What is the minimum attendance required?", "How much attendance do I need to maintain?", "Is there a compulsory attendance policy?", "What happens if my attendance is low?", "What is the percentage of attendance needed for exams?", "minimum attendance kitni chahiye?", "kitni attendance maintain karni hai?", "attendance kam ho to kya hoga?", "ochhama ochhi ketli hajari joiye?", "mare ketli attendance joiye?", "jo mari hajari ochhi hoy to shu thay?"],
        "hi": ["न्यूनतम कितनी उपस्थिति आवश्यक है?", "मुझे कितनी उपस्थिति बनाए रखनी होगी?", "कम उपस्थिति होने पर क्या होता है?"],
        "gu": ["ઓછામાં ઓછી કેટલી હાજરી જરૂરી છે?", "મારે કેટલી હાજરી જાળવવી પડશે?", "જો મારી હાજરી ઓછી હોય તો શું થાય?"]
    }},
    {"intentName": "ask_office_hours", "trainingPhrases": {
        "en": ["What are the office hours?", "When is the admin office open?", "Office timings", "Till what time is the office open?", "office hours kya hain?", "admin office kab tak open rehta hai?", "office no time shu chhe?", "admin office kyare khulli hoy chhe?"],
        "hi": ["कार्यालय का समय क्या है?", "एडमिन ऑफिस कब खुला रहता है?"],
        "gu": ["ઓફિસનો સમય શું છે?", "એડમિન ઓફિસ ક્યારે ખુલ્લી રહે છે?"]
    }},
    {"intentName": "ask_passing_criteria", "trainingPhrases": {
        "en": ["What is the passing criteria for exams?", "How many marks are needed to pass a subject?", "What is the passing percentage?", "Tell me about the passing marks.", "How is the final grade calculated?", "exam pass karne ka criteria kya hai?", "subject me pass hone ke liye kitne marks chahiye?", "passing percentage kitna hai?", "exam pass karva mate no criteria shu chhe?", "ek subject ma pass thava mate ketla marks joiye?", "passing takavari ketli chhe?"],
        "hi": ["परीक्षाओं के लिए उत्तीर्ण होने का मानदंड क्या है?", "एक विषय में उत्तीर्ण होने के लिए कितने अंकों की आवश्यकता होती है?", "उत्तीर्ण प्रतिशत क्या है?"],
        "gu": ["પરીક્ષાઓ માટે પાસિંગ માપદંડ શું છે?", "એક વિષયમાં પાસ થવા માટે કેટલા માર્ક્સની જરૂર છે?", "પાસિંગ ટકાવારી કેટલી છે?"]
    }},
    {"intentName": "ask_sports_facilities", "trainingPhrases": {
        "en": ["What sports facilities are available?", "Is there a gym?", "Tell me about the sports complex.", "Can we play cricket on campus?", "Do you have a basketball court?", "konsi sports facilities available hain?", "gym hai kya?", "ramatgamat ni kai suvidhao uplabdh chhe?", "shu gym chhe?"],
        "hi": ["कौन सी खेल सुविधाएं उपलब्ध हैं?", "क्या जिम है?"],
        "gu": ["રમતગમતની કઈ સુવિધાઓ ઉપલબ્ધ છે?", "શું જિમ છે?"]
    }},
    {"intentName": "ask_student_support_committees", "trainingPhrases": {
        "en": ["What student committees are there?", "Tell me about student support.", "Are there any clubs I can join?", "Who can I contact for student support?", "List of student committees.", "konsi student committees hain?", "student support ke bare me batao.", "kai vidyarthi samitio chhe?", "vidyarthi support vishe mane kaho."],
        "hi": ["कौन सी छात्र समितियां हैं?", "छात्र सहायता के बारे में बताएं।"],
        "gu": ["કઈ વિદ્યાર્થી સમિતિઓ છે?", "વિદ્યાર્થી સપોર્ટ વિશે મને કહો."]
    }},
    {"intentName": "ask_transport_facility", "trainingPhrases": {
        "en": ["Is there a bus service?", "Tell me about the college transport facility.", "How can I use the college bus?", "What are the bus routes?", "Is transport available from my area?", "bus service hai kya?", "college transport facility ke bare me batao.", "bus seva chhe?", "college parivahan suvidha vishe mane kaho."],
        "hi": ["क्या बस सेवा है?", "कॉलेज परिवहन सुविधा के बारे में बताएं।"],
        "gu": ["શું બસ સેવા છે?", "કોલેજ પરિવહન સુવિધા વિશે મને કહો."]
    }},
    {"intentName": "ask_what_if_fail", "trainingPhrases": {
        "en": ["What if I fail a subject?", "What happens if I get a backlog?", "Is there a re-exam if I fail?", "Tell me about the supplementary exams.", "What is the process for reappearing in an exam?", "agar main ek subject me fail ho gaya to kya hoga?", "backlog lagne par kya hota hai?", "fail hone par re-exam hota hai kya?", "jo hu koi vishay ma fail thau to shu?", "jo mane backlog aave to shu thay?", "jo hu fail thau to fari exam levay chhe?"],
        "hi": ["यदि मैं किसी विषय में फेल हो जाता हूं तो क्या होगा?", "यदि मुझे बैकलॉग मिलता है तो क्या होता है?", "क्या फेल होने पर दोबारा परीक्षा होती है?"],
        "gu": ["જો હું કોઈ વિષયમાં નાપાસ થાઉં તો શું?", "જો મને બેકલોગ આવે તો શું થાય?", "જો હું નાપાસ થાઉં તો ફરી પરીક્ષા લેવાય છે?"]
    }},
    {"intentName": "ask_wifi_access", "trainingPhrases": {
        "en": ["How to get wifi access?", "What is the wifi password?", "How do I connect to campus wifi?", "Is there free wifi for students?", "Tell me the procedure to get wifi password.", "wifi access kaise milega?", "wifi ka password kya hai?", "wifi access kevi rite malshe?", "wifi no password shu chhe?"],
        "hi": ["वाईफाई का उपयोग कैसे करें?", "वाईफाई का पासवर्ड क्या है?"],
        "gu": ["કેમ્પસ વાઇફાઇથી કેવી રીતે કનેક્ટ કરવું?", "શું વિદ્યાર્થીઓ માટે મફત વાઇફાઇ છે?"]
    }},
    {"intentName": "find_academic_calendar", "trainingPhrases": {
        "en": ["Where can I find the academic calendar?", "Show me the academic calendar for this year.", "I need the list of important academic dates.", "When does the semester start and end?", "Academic schedule.", "academic calendar kahan milega?", "is saal ka academic calendar dikhao.", "academic calendar kyathi malshe?", "aa varsh nu academic calendar batavo."],
        "hi": ["मुझे अकादमिक कैलेंडर कहां मिल सकता है?", "इस वर्ष का अकादमिक कैलेंडर दिखाएं।"],
        "gu": ["મને શૈક્ષણિક કેલેન્ડર ક્યાંથી મળશે?", "મને આ વર્ષનું શૈક્ષણિક કેલેન્ડર બતાવો."]
    }},
    {"intentName": "find_exam_timetable", "trainingPhrases": {
        "en": ["Where can I find the exam timetable?", "Show me the exam schedule.", "When are the final exams?", "I need the timetable for mid-semester exams.", "Exam dates.", "exam timetable kahan milega?", "exam schedule dikhao.", "exam timetable kyathi malshe?", "pariksha nu samaypatrak batavo."],
        "hi": ["मुझे परीक्षा की समय सारिणी कहां मिल सकती है?", "परीक्षा का कार्यक्रम दिखाएं।"],
        "gu": ["મને પરીક્ષાનું સમયપત્રક ક્યાંથી મળશે?", "પરીક્ષાનું સમયપત્રક બતાવો."]
    }},
    {"intentName": "find_fee_structure", "trainingPhrases": {
        "en": ["What is the fee structure?", "Show me the fee details for B.Tech.", "How much are the tuition fees?", "I need the fee structure for the first year.", "Fee details.", "fee structure kya hai?", "B.Tech ke liye fee details dikhao.", "fee nu madkhu shu chhe?", "B.Tech mate fee ni vigato batavo."],
        "hi": ["शुल्क संरचना क्या है?", "बी.टेक के लिए शुल्क विवरण दिखाएं।"],
        "gu": ["ફીનું માળખું શું છે?", "બી.ટેક. માટે ફીની વિગતો બતાવો."]
    }},
    {"intentName": "find_grievance_cells", "trainingPhrases": {
        "en": ["List of grievance cells", "Who to contact for grievances?", "Tell me about the different grievance committees.", "Where can I find details about the anti-ragging cell?", "Contact for women's cell.", "grievance cells ki list", "grievances ke liye kis se contact karein?", "fariyad nivaran cell ni yadi", "fariyado mate kono sampark karvo?"],
        "hi": ["शिकायत प्रकोष्ठों की सूची", "शिकायतों के लिए किससे संपर्क करें?"],
        "gu": ["ફરિયાદ નિવારણ સેલની યાદી", "ફરિયાદો માટે કોનો સંપર્ક કરવો?"]
    }},
    {"intentName": "find_holidays_notices", "trainingPhrases": {
        "en": ["List of holidays", "When is the next holiday?", "Show me the holiday calendar.", "Are we off for Diwali?", "Holiday notices.", "holidays ki list", "next holiday kab hai?", "rajao ni yadi", "aagami raja kyare chhe?"],
        "hi": ["छुट्टियों की सूची", "अगली छुट्टी कब है?"],
        "gu": ["રજાઓની યાદી", "આગામી રજા ક્યારે છે?"]
    }},
    {"intentName": "find_policies_rules", "trainingPhrases": {
        "en": ["Where can I find college rules?", "Show me the student handbook.", "I need to read the code of conduct.", "Rules and regulations for students.", "Policy documents.", "college ke rules kahan milenge?", "student handbook dikhao.", "college na niyamo kyathi malshe?", "vidyarthi pustika batavo."],
        "hi": ["मुझे कॉलेज के नियम कहां मिल सकते हैं?", "छात्र पुस्तिका दिखाएं।"],
        "gu": ["મને કોલેજના નિયમો ક્યાંથી મળશે?", "વિદ્યાર્થી પુસ્તિકા બતાવો."]
    }},
    {"intentName": "find_previous_question_papers", "trainingPhrases": {
        "en": ["Where can I find previous year question papers?", "I need old exam papers.", "Can you provide last year's question papers?", "Show me the question paper archive.", "Previous papers for the final exams.", "previous year question papers kahan milenge?", "purane exam papers chahiye.", "pichle saal ke question papers de sakte ho?", "pachhla varsh na question paper kyathi malshe?", "mare juna exam na paper joiye chhe.", "tame gaya varsh na question paper aapi shako?"],
        "hi": ["मुझे पिछले वर्ष के प्रश्न पत्र कहाँ मिल सकते हैं?", "मुझे पुराने परीक्षा पत्र चाहिए।", "क्या आप पिछले साल के प्रश्न पत्र प्रदान कर सकते हैं?"],
        "gu": ["મને પાછલા વર્ષના પ્રશ્નપત્રો ક્યાંથી મળશે?", "મારે જૂના પરીક્ષાના પેપર જોઈએ છે.", "શું તમે ગયા વર્ષના પ્રશ્નપત્રો આપી શકો છો?"]
    }},
    {"intentName": "find_syllabus", "trainingPhrases": {
        "en": ["Where can I find the syllabus?", "Can you give me the syllabus for computer engineering?", "I need the first year syllabus.", "Show me the syllabus.", "Syllabus for the third semester.", "syllabus kahan milega?", "computer engineering ka syllabus de sakte ho?", "first year ka syllabus chahiye.", "syllabus kyathi malshe?", "computer engineering no syllabus aapi shako?", "mare first year no syllabus joiye chhe."],
        "hi": ["मुझे सिलेबस कहाँ मिल सकता है?", "क्या आप मुझे कंप्यूटर इंजीनियरिंग का सिलेबस दे सकते हैं?", "मुझे पहले वर्ष का सिलेबस चाहिए।"],
        "gu": ["મને સિલેબસ ક્યાંથી મળશે?", "શું તમે મને કમ્પ્યુટર એન્જિનિયરિંગનો સિલેબસ આપી શકો છો?", "મારે પ્રથમ વર્ષનો સિલેબસ જોઈએ છે."]
    }}
]

def create_dialogflow_files():
    """
    Generates the necessary JSON files for a multilingual Dialogflow agent import
    based on the user's specified working format.
    """
    output_dir = "dialogflow_agent_files"
    intents_dir = os.path.join(output_dir, "intents")
    os.makedirs(intents_dir, exist_ok=True)
    
    # --- Create agent.json using the user's specified format ---
    agent_data = {
      "language": "en",
      "supportedLanguages": [
        "hi",
        "gu"
      ],
      "webhook": {"available": True},
      "defaultTimezone": "Asia/Kolkata"
    }
    with open(os.path.join(output_dir, "agent.json"), "w", encoding='utf-8') as f:
        json.dump(agent_data, f, indent=2, ensure_ascii=False)

    # --- Create the required package.json ---
    package_data = {"version": "1.0.0"}
    with open(os.path.join(output_dir, "package.json"), "w", encoding='utf-8') as f:
        json.dump(package_data, f, indent=2, ensure_ascii=False)

    # --- Loop through the intent data and create files for each language ---
    for intent in INTENT_DATA:
        intent_name = intent["intentName"]
        
        # 1. Create the main intent file
        intent_file_path = os.path.join(intents_dir, f"{intent_name}.json")
        intent_content = {
            "name": intent_name,
            "auto": True,
            "webhookUsed": True,
            "responses": [{"parameters": [], "messages": [], "defaultResponsePlatforms": {}}]
        }
        with open(intent_file_path, "w", encoding='utf-8') as f:
            json.dump(intent_content, f, indent=2, ensure_ascii=False)

        # 2. Create the training phrases files for each language specified
        for lang_code, phrases in intent["trainingPhrases"].items():
            usersays_file_path = os.path.join(intents_dir, f"{intent_name}_usersays_{lang_code}.json")
            usersays_content = []
            for phrase in phrases:
                usersays_content.append({
                    "data": [{"text": phrase, "userDefined": False}],
                    "isTemplate": False,
                    "count": 0,
                })
            
            with open(usersays_file_path, "w", encoding='utf-8') as f:
                json.dump(usersays_content, f, indent=2, ensure_ascii=False)

    print(f"✅ Successfully created all multilingual intent files in the '{output_dir}' folder.")
    print("You can now zip this folder and import it into Dialogflow.")

if __name__ == "__main__":
    create_dialogflow_files()