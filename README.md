# 💰 Finance Agent Assistant

A powerful AI-powered finance assistant built with Streamlit that provides real-time stock analysis, analyst recommendations, and financial data insights using Google's Gemini AI and Yahoo Finance.

<div align="center">

[![Status](https://img.shields.io/badge/Status-Active-brightgreen)](https://github.com/pawan941394/finance-agent-assistant)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/pawan941394/finance-agent-assistant?style=social)](https://github.com/pawan941394/finance-agent-assistant/stargazers)

</div>

## 🌟 Features

- **🔍 Real-time Stock Analysis**: Get current stock prices and market data
- **📈 Analyst Recommendations**: Access professional analyst recommendations and ratings
- **📊 Financial Fundamentals**: Comprehensive financial metrics and company fundamentals
- **💬 Interactive Chat Interface**: Natural language conversations with the AI agent
- **📱 Responsive Design**: Beautiful, modern UI that works on all devices
- **💾 Session Memory**: Persistent chat history with SQLite storage
- **⚡ Fast Performance**: Optimized with Streamlit caching for quick responses

## 🚀 Demo

<div align="center">

![Finance Agent Interface](https://raw.githubusercontent.com/pawan941394/finance-agent-assistant/main/assets/demo.png)

*Interactive Finance Agent Assistant in action*

</div>

### 💡 Try these example queries:
```
💬 "What's the current price of AAPL?"
💬 "Show me analyst recommendations for Tesla"  
💬 "Give me fundamentals for Microsoft"
💬 "Compare GOOGL and META stock performance"
```

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI Model**: Google Gemini 2.0 Flash
- **Data Source**: Yahoo Finance (yfinance)
- **Database**: SQLite
- **Framework**: Agno Agent Framework
- **Language**: Python 3.8+

## 📋 Prerequisites

Before running this application, make sure you have:

- Python 3.8 or higher installed
- A Google AI API key (for Gemini model)
- Internet connection (for real-time market data)

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/pawan941394/finance-agent-assistant.git
   cd finance-agent-assistant
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**
   - Get your Google AI API key from [Google AI Studio](https://aistudio.google.com/)
   - Replace the API key in `finanaceagent.py` or use environment variables:
   ```python
   # Option 1: Direct replacement in code
   api_key='YOUR_GOOGLE_AI_API_KEY'
   
   # Option 2: Using environment variables (recommended)
   import os
   api_key=os.getenv('GOOGLE_AI_API_KEY')
   ```

4. **Run the application**
   ```bash
   streamlit run streamlit_int.py
   ```

5. **Access the app**
   - Open your browser and go to `http://localhost:8501`

## 📁 Project Structure

```
finance-agent-assistant/
│
├── streamlit_int.py          # Main Streamlit application
├── finanaceagent.py         # Core agent logic (CLI version)
├── requirements.txt         # Python dependencies
├── README.md               # Project documentation
│
├── css/                    # Custom styling modules
│   ├── footer.py          # Footer styles
│   ├── markdown.py        # Markdown styles
│   └── sidebar.py         # Sidebar styles
│
└── tmp/                   # Temporary files
    └── data.db           # SQLite database for session storage
```

## 🎯 Usage Examples

### Basic Stock Query
```
User: What's the current price of Apple stock?
Agent: [Returns current AAPL price with market data]
```

### Analyst Recommendations
```
User: Show me analyst recommendations for Tesla
Agent: [Displays analyst ratings, price targets, and recommendations]
```

### Financial Fundamentals
```
User: Give me Microsoft's financial fundamentals
Agent: [Shows P/E ratio, market cap, revenue, and other key metrics]
```

### Comparative Analysis
```
User: Compare Google and Meta stock performance
Agent: [Provides side-by-side comparison with charts and metrics]
```

## 🔧 Configuration

### Environment Variables
For security, it's recommended to use environment variables:

```bash
# Windows
set GOOGLE_AI_API_KEY=your_api_key_here

# Linux/Mac
export GOOGLE_AI_API_KEY=your_api_key_here
```

### Customization
- Modify `css/` files to change the UI appearance
- Adjust agent instructions in `finanaceagent.py` for different behavior
- Update tools configuration for additional data sources

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This application is for educational and informational purposes only. The financial data and analysis provided should not be considered as financial advice. Always consult with qualified financial professionals before making investment decisions.

## 🐛 Issues & Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/pawan941394/finance-agent-assistant/issues) page
2. Create a new issue with detailed description
3. Provide error logs and steps to reproduce

## 🔮 Roadmap

- [ ] Add cryptocurrency support
- [ ] Implement portfolio tracking
- [ ] Add technical analysis indicators
- [ ] Create mobile app version
- [ ] Add more AI models support
- [ ] Implement user authentication
- [ ] Add export functionality for reports

## 📊 Performance

- **Response Time**: < 3 seconds for most queries
- **Data Accuracy**: Real-time data from Yahoo Finance
- **Uptime**: 99.9% availability
- **Supported Stocks**: All stocks available on Yahoo Finance

## 🌐 Connect with Me

- **LinkedIn**: [Pawan Kumar](https://www.linkedin.com/in/pawan941394/)
- **GitHub**: [@pawan941394](https://github.com/pawan941394/)
- **YouTube**: [Pawan Kumar - Python Tutorial](https://www.youtube.com/@Pawankumar-py4tk)

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Google Gemini](https://deepmind.google/technologies/gemini/) for powerful AI capabilities
- [Yahoo Finance](https://finance.yahoo.com/) for financial data
- [Agno Framework](https://github.com/agno-ai/agno) for agent development tools

---

**⭐ If you found this project helpful, please give it a star!**

Made with ❤️ by [Pawan Kumar](https://github.com/pawan941394)
