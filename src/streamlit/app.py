import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Streamlit başlığı
st.title("Hisse Senedi Fiyatları ve Hedef Fiyat Tahminleri")

# Kullanıcıdan hisse senedi sembolü alma
ticker_symbol = st.text_input("Hisse Senedi Sembolünü Girin (örn: AAPL, TSLA)", "AAPL")

# Hisse senedi verilerini çekme
stock_data = yf.Ticker(ticker_symbol)
stock_price = stock_data.history(period="1y")  # Son 1 yıllık veriler

# Hedef fiyat tahminlerini alma
recommendations = stock_data.recommendations

if recommendations is not None and not recommendations.empty:
    # En son hedef fiyat tahminini al
    latest_target = recommendations.iloc[-1]
    target_price = latest_target['to']  # Hedef fiyat
    target_date = latest_target.name  # Hedef fiyat tarihi
else:
    target_price = None
    target_date = None

# Kapanış fiyatlarını ve tahminleri görselleştirme
fig, ax = plt.subplots()

# Gerçek kapanış fiyatlarını çiz
ax.plot(stock_price.index, stock_price['Close'], label="Gerçek Fiyatlar", color="blue")

# Eğer hedef fiyat tahmini varsa, grafiğe ekle
if target_price is not None:
    ax.axhline(y=target_price, color='red', linestyle='--', label=f"Hedef Fiyat Tahmini: {target_price} ({target_date.date()})")
else:
    st.write("Hedef fiyat tahmini bulunamadı.")

# Grafik detayları
ax.set_xlabel("Tarih")
ax.set_ylabel("Fiyat (USD)")
ax.legend()

# Grafiği Streamlit ile göster
st.pyplot(fig)
