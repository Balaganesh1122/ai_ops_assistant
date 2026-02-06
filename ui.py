import streamlit as st
from dotenv import load_dotenv
import os

# Import agents directly
from agents.planner import create_plan
from agents.executor import execute_plan
from agents.verifier import verify_and_format

# Load environment variables
load_dotenv()

st.set_page_config(page_title="AI Ops Assistant", page_icon="🤖")

st.title("🤖 AI Operations Assistant")

task = st.text_area("Enter your task", placeholder="e.g., Check the weather in Mumbai")

if st.button("Run Task"):
    if not task:
        st.warning("Please enter a task first.")
    else:
        try:
            with st.spinner("🧠 Agents are working..."):
                # 1. Plan
                plan = create_plan(task)
                if "error" in plan:
                    st.error(f"Planning failed: {plan}")
                    st.stop()
                
                # 2. Execute
                execution_results = execute_plan(plan)
                
                # 3. Verify
                final_output = verify_and_format(task, plan, execution_results)
            
            st.success("Analysis Complete!")
            
            # Display Final Result
            st.markdown("### 📝 Final Answer")
            st.info(final_output.get("summary", "No summary available"))
            
            with st.expander("🔍 Use Developer Details"):
                st.json(final_output)

        except Exception as e:
            st.error(f"An internal error occurred: {e}")
