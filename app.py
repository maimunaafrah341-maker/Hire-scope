import streamlit as st
from scraper import scrape_candidates
from agent import analyse_candidate

st.set_page_config(page_title="HireScope", layout="wide")

st.title("🔍 HireScope")
st.subheader("Hiring Risk & Blindspot Detector — Powered by Bright Data + Featherless AI")

st.markdown("---")

st.header("Step 1: Enter Candidate LinkedIn URLs")
urls_input = st.text_area(
    "Paste LinkedIn profile URLs (one per line)",
    placeholder="https://www.linkedin.com/in/example1\nhttps://www.linkedin.com/in/example2"
)

if st.button("🚀 Analyse Candidates", type="primary"):
    if not urls_input.strip():
        st.error("Please enter at least one LinkedIn URL!")
    else:
        urls = [url.strip() for url in urls_input.strip().split("\n") if url.strip()]
        
        st.markdown("---")
        st.header("Step 2: Scraping Real Data via Bright Data...")
        
        with st.spinner("Fetching candidate profiles from LinkedIn..."):
            candidates = scrape_candidates(urls)
        
        if "error" in candidates:
            st.error(f"Scraping error: {candidates['error']}")
        else:
            st.success(f"✅ Successfully scraped {len(urls)} candidate(s)!")
            
            st.markdown("---")
            st.header("Step 3: AI Agent Analysing Hiring Risks...")
            
            if isinstance(candidates, list):
                candidate_list = candidates
            else:
                candidate_list = [candidates]
            
            for i, candidate in enumerate(candidate_list):
                st.subheader(f"Candidate {i+1}")
                
                with st.spinner(f"Running 3-step AI analysis on Candidate {i+1}..."):
                    result = analyse_candidate(candidate)
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.markdown("### 📋 Profile Analysis")
                    st.write(result["analysis"])
                
                with col2:
                    st.markdown(" Risks & Blindspots")
                    st.write(result["risks"])
                
                with col3:
                    st.markdown(" Hiring Decision")
                    st.write(result["decision"])
                
                st.markdown("---")

st.caption("HireScope — Built with Bright Data + Featherless AI + Google cloud + Streamlit")