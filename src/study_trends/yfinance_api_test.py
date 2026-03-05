from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))

from utils.ollama_model import get_chat_model
import yfinance as yf
import matplotlib.pyplot as plt
from langchain_core.prompts import ChatPromptTemplate
from utils.prompts import get_sytem_prompt
from utils.pretty_print import pretty_print


def get_trends(ticker, start_date, end_date):
    # Fetch historical data for the specified ticker and date range
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    
    # Check if data is retrieved successfully
    if stock_data.empty:
        print(f"No data found for {ticker} between {start_date} and {end_date}.")
        return
    
    # Display the retrieved data
    print(stock_data)
    return stock_data

def plot_trends(stock_data):
    # Plot the closing price trend
    stock_data['Close'].plot(title='Closing Price Trend')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.show()

def study_trends(stock_data):
    system_msg = get_sytem_prompt("generate a system prompt to guide model behaviour to study charts and grab news or other sources to analyze the stock data")

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_msg),
        ("human", "Analyze the following stock data and provide insights: {stock_data}")
    ])

    model = get_chat_model()
    chain = prompt | model
    response = chain.invoke({"stock_data": stock_data.to_string()})

    pretty_print(response.content)
    return response

if  __name__ == "__main__":
    # Define the stock ticker, start date, and end date
    ticker = "GOOG" 
    start_date = "2026-01-01"
    end_date = "2026-01-31"
    
    # Call the function to study trends
    data = get_trends(ticker, start_date, end_date)

    if data is not None: 
        plot_trends(data)
        study_trends(data)