from fastapi import FastAPI
import pandas as pd
import yfinance as yf

yf_api=FastAPI(title="My yahoo finance api",description="This Api allows get the Lastest price of our favorite Market Assets!")

@yf_api.get("/")
def root():
    return {"Message":"This is the root, please visit /docs"}

@yf_api.get("/TSLA")
def asset_price():
    asset=yf.Ticker("TSLA")
    asset_history=asset.history(period="1d",interval="1m")
    df_aaset=pd.DataFrame(asset_history)
    last_value=df_aaset["Close"][-1]
    return {"Asset":"TSLA","Value":last_value}

@yf_api.get("/AMZN")
def asset_price():
    asset=yf.Ticker("AMZN")
    asset_history=asset.history(period="1d",interval="1m")
    df_aaset=pd.DataFrame(asset_history)
    last_value=df_aaset["Close"][-1]
    return {"Asset":"AMZN","Value":last_value}

@yf_api.get("/BABA")
def asset_price():
    asset=yf.Ticker("BABA")
    asset_history=asset.history(period="1d",interval="1m")
    df_aaset=pd.DataFrame(asset_history)
    last_value=df_aaset["Close"][-1]
    return {"Asset":"BABA","Value":last_value}

@yf_api.get("/NFLX")
def asset_price():
    asset=yf.Ticker("NFLX")
    asset_history=asset.history(period="1d",interval="1m")
    df_aaset=pd.DataFrame(asset_history)
    last_value=df_aaset["Close"][-1]
    return {"Asset":"NFLX","Value":last_value}

