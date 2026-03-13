import os
import sys
import google.generativeai as genai
from pinecone import Pinecone
from dotenv import load_dotenv
import traceback

# Setup
sys.stdout.reconfigure(encoding='utf-8')
load_dotenv()

def test_rag_pipeline():
    print("--- Verifying RAG Pipeline Components ---", flush=True)
    
    # 1. Check Environment Variables
    print("\n1. Checking Environment Variables...", end=" ", flush=True)
    gemini_key = os.getenv("GEMINI_API_KEY")
    pinecone_key = os.getenv("PINECONE_API_KEY")
    
    if not gemini_key:
        print("❌ Failed: GEMINI_API_KEY missing", flush=True)
        return
    if not pinecone_key:
        print("❌ Failed: PINECONE_API_KEY missing", flush=True)
        return
    print("✅ Present", flush=True)

    # 2. Test Gemini Embeddings
    print("2. Testing Gemini Embeddings...", end=" ", flush=True)
    try:
        genai.configure(api_key=gemini_key)
        test_text = "This is a test query."
        embedding_model = "models/text-embedding-004"
        
        embedding = genai.embed_content(model=embedding_model, content=test_text, task_type="RETRIEVAL_QUERY")["embedding"]
        if embedding and len(embedding) > 0:
            print("✅ Success", flush=True)
        else:
            print("⚠️ Generated empty embedding", flush=True)
            return
    except Exception as e:
        print(f"❌ Failed: {e}", flush=True)
        return

    # 3. Test Pinecone Connection & Query
    print("3. Testing Pinecone Connection...", end=" ", flush=True)
    try:
        pc = Pinecone(api_key=pinecone_key)
        index_name = 'sih-rag-index'
        index = pc.Index(index_name)
        
        # Perform a dummy query
        results = index.query(vector=embedding, top_k=1, include_metadata=True)
        print("✅ Success", flush=True)
        
        if results['matches']:
            print(f"   ℹ️ Found {len(results['matches'])} matches in Pinecone.", flush=True)
        else:
            print("   ℹ️ Connection successful, but no matches found (Index might be empty).", flush=True)
            
    except Exception as e:
        print(f"❌ Failed: {e}", flush=True)
        return

    # 4. Test Gemini Generation (Final RAG Step)
    print("4. Testing Gemini Generation...", end=" ", flush=True)
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content("Hello, this is a test.")
        if response.text:
            print("✅ Success", flush=True)
        else:
            print("⚠️ Empty response", flush=True)
    except Exception as e:
        print(f"❌ Failed: {e}", flush=True)

if __name__ == "__main__":
    test_rag_pipeline()
    print("\nDone.", flush=True)
