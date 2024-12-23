import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
import random

# Algoritma Iteratif
def check_stock_iterative(stock_list, threshold):
    items_to_restock = {}
    for item, stock in stock_list.items():
        if stock < threshold:
            items_to_restock[item] = stock
    return items_to_restock

# Algoritma Rekursif
def check_stock_recursive(stock_list, threshold, keys=None, index=0, items_to_restock=None):
    if items_to_restock is None:
        items_to_restock = {}
    if keys is None:
        keys = list(stock_list.keys())
    if index == len(keys):
        return items_to_restock
    item = keys[index]
    if stock_list[item] < threshold:
        items_to_restock[item] = stock_list[item]
    return check_stock_recursive(stock_list, threshold, keys, index + 1, items_to_restock)

# Fungsi untuk mengukur waktu eksekusi
def measure_execution_time(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time

# UI Streamlit
st.title("Perbandingan Algoritma Iteratif dan Rekursif dalam Manajemen Stok Barang")

# Input jumlah data dan threshold
max_n = st.number_input("Masukkan jumlah maksimum item dalam inventaris:", min_value=1, value=50)
threshold = st.number_input("Masukkan batas minimum stok:", min_value=1, value=5)

if st.button("Jalankan Algoritma"):
    # Data untuk grafik
    iterative_times = []
    recursive_times = []
    x_values = list(range(1, max_n + 1))

    for n in x_values:
        # Membuat daftar stok barang secara acak dengan nama barang
        item_names = [f"Barang-{i}" for i in range(1, n + 1)]
        stock_values = np.random.randint(1, 20, size=n)
        stock_list = dict(zip(item_names, stock_values))

        # Mengukur waktu untuk algoritma iteratif
        iterative_time = measure_execution_time(check_stock_iterative, stock_list, threshold)
        iterative_times.append(iterative_time)

        # Mengukur waktu untuk algoritma rekursif
        recursive_time = measure_execution_time(check_stock_recursive, stock_list, threshold)
        recursive_times.append(recursive_time)

    # Menampilkan grafik perbandingan
    fig, ax = plt.subplots()
    ax.plot(x_values, iterative_times, label="Iteratif", marker='o', color='magenta')
    ax.plot(x_values, recursive_times, label="Rekursif", marker='o', color='green')
    ax.set_xlabel("Jumlah Barang")
    ax.set_ylabel("Waktu Eksekusi (detik)")
    ax.set_title("Perbandingan Waktu Eksekusi Berdasarkan Jumlah Barang")
    ax.legend()
    st.pyplot(fig)
