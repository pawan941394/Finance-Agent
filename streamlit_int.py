import streamlit as st
import sys
import os
from agno.agent import Agent
from agno.storage.sqlite import SqliteStorage
from agno.tools.yfinance import YFinanceTools
from agno.models.google import Gemini
from css.markdown import css
from css.sidebar import sidebar
from css.footer import footer
# Page configuration
st.set_page_config(
    page_title="Finance Agent Assistant",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown(f'{css()}', unsafe_allow_html=True)

# Initialize the agent
@st.cache_resource
def initialize_agent():
    """Initialize the finance agent with proper configuration"""
    try:
        agent = Agent(
            model=Gemini(id="gemini-2.0-flash-exp", api_key='your api key'),
            tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
            description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
            instructions=["Format your response using markdown and use tables to display data where possible."],
            session_id="streamlit_session",
            storage=SqliteStorage(table_name="agent_sessions", db_file="tmp/data.db"),
            add_history_to_messages=True,
            num_history_runs=3,
        )
        return agent
    except Exception as e:
        st.error(f"Error initializing agent: {str(e)}")
        return None

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'agent' not in st.session_state:
    st.session_state.agent = initialize_agent()

# Main header
st.markdown('<h1 class="main-header">💰 Finance Agent Assistant</h1>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("📊 About")
    st.markdown(f'{sidebar()}', unsafe_allow_html=True)

    st.header("🛠️ Quick Actions")
    if st.button("Clear Chat History", type="secondary"):
        st.session_state.messages = []
        st.rerun()
    
    st.header("💡 Example Queries")
    st.markdown("""
    Try asking:
    - "What's the current price of AAPL?"
    - "Show me analyst recommendations for Tesla"
    - "Give me fundamentals for Microsoft"
    - "Compare GOOGL and META stock performance"
    """)

# Main chat interface
col1, col2 = st.columns([9, 1])

with col1:
    # Display chat messages
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"""
            <div class="chat-message user-message">
                <strong>You:</strong> {message["content"]}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="chat-message agent-message">
                <strong>Finance Agent:</strong>
            </div>
            """, unsafe_allow_html=True)
            st.markdown(message["content"])

    # Chat input
    user_input = st.chat_input("Ask me about stocks, market analysis, or financial data...")

    if user_input:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Display user message immediately
        st.markdown(f"""
        <div class="chat-message user-message">
            <strong>You:</strong> {user_input}
        </div>
        """, unsafe_allow_html=True)
        
        # Get agent response
        if st.session_state.agent:
            with st.spinner("Finance Agent is analyzing..."):
                try:
                    # Get the agent's response
                    response = st.session_state.agent.run(user_input)
                    agent_response = response.content if hasattr(response, 'content') else str(response)
                    
                    # Add agent response to chat history
                    st.session_state.messages.append({"role": "agent", "content": agent_response})
                    
                    # Display agent response
                    st.markdown(f"""
                    <div class="chat-message agent-message">
                        <strong>Finance Agent:</strong>
                    </div>
                    """, unsafe_allow_html=True)
                    st.markdown(agent_response)
                    
                except Exception as e:
                    error_message = f"Sorry, I encountered an error: {str(e)}"
                    st.error(error_message)
                    st.session_state.messages.append({"role": "agent", "content": error_message})
        else:
            error_message = "Agent is not initialized. Please check your configuration."
            st.error(error_message)
            st.session_state.messages.append({"role": "agent", "content": error_message})
        
        # Rerun to update the chat display
        st.rerun()


# Footer
st.markdown("---")
st.markdown(f'{footer()}', unsafe_allow_html=True)
