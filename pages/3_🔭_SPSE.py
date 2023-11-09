#####################################################################################
# Source code: Dashboard Bukan Amel                                                 #
#-----------------------------------------------------------------------------------#
# Dashboard ini dibuat oleh:                                                        #
# Nama          : Kurnia Ramadhan, ST.,M.Eng                                        #
# Jabatan       : Sub Koordinator Pengelolaan Informasi LPSE                        #
# Instansi      : Biro Pengadaan Barang dan Jasa Setda Prov. Kalbar                 #
# Email         : kramadhan@gmail.com                                               #
# URL Web       : https://github.com/blogramadhan                                   #
#-----------------------------------------------------------------------------------#
# Hak cipta milik Allah SWT, source code ini silahkan dicopy, di download atau      #
# di distribusikan ke siapa saja untuk bahan belajar, atau untuk dikembangkan lagi  #
# lebih lanjut, btw tidak untuk dijual ya.                                          #
#                                                                                   #
# Jika teman-teman mengembangkan lebih lanjut source code ini, agar berkenan untuk  #
# men-share code yang teman-teman kembangkan lebih lanjut sebagai bahan belajar     #
# untuk kita semua.                                                                 #
#-----------------------------------------------------------------------------------#
# @ Pontianak, 2023                                                                 #
#####################################################################################

# Import Library
import duckdb
import openpyxl
import streamlit as st
import pandas as pd
import plotly.express as px
# Import library currency
from babel.numbers import format_currency
# Import library Aggrid
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
# Import Streamlit Extras
from streamlit_extras.metric_cards import style_metric_cards
# Import fungsi pribadi
from fungsi import *

# Konfigurasi variabel lokasi UKPBJ
daerah = ["KAB. MUSI BANYUASIN"]

tahuns = ["2023", "2022"]

pilih = st.sidebar.selectbox("Pilih UKPBJ yang diinginkan :", daerah)
tahun = st.sidebar.selectbox("Pilih Tahun :", tahuns)

if pilih == "KAB. MUSI BANYUASIN":
    kodeFolder = "muba"

# Persiapan Dataset
con = duckdb.connect(database=':memory:')

## Akses file dataset format parquet dari Google Cloud Storage via URL Public

### Dataset SPSE Tender
DatasetSPSETenderPengumuman = f"https://storage.googleapis.com/bukanamel/{kodeFolder}/spse/SPSETenderPengumuman{tahun}.parquet"
DatasetSPSETenderSelesai = f"https://storage.googleapis.com/bukanamel/{kodeFolder}/spse/SPSETenderSelesai{tahun}.parquet"
DatasetSPSETenderSelesaiNilai = f"https://storage.googleapis.com/bukanamel/{kodeFolder}/spse/SPSETenderSelesaiNilai{tahun}.parquet"
DatasetSPSETenderSPPBJ = f"https://storage.googleapis.com/bukanamel/{kodeFolder}/spse/SPSETenderEkontrakSPPBJ{tahun}.parquet"
DatasetSPSETenderKontrak = f"https://storage.googleapis.com/bukanamel/{kodeFolder}/spse/SPSETenderEkontrakKontrak{tahun}.parquet"
DatasetSPSETenderSPMK = f"https://storage.googleapis.com/bukanamel/{kodeFolder}/spse/SPSETenderEkontrakSPMKSPP{tahun}.parquet"
DatasetSPSETenderBAST = f"https://storage.googleapis.com/bukanamel/{kodeFolder}/spse/SPSETenderEkontrakBAPBAST{tahun}.parquet"

### Dataset SPSE Non Tender
DatasetSPSENonTenderPengumuman = f"https://storage.googleapis.com/bukanamel/{kodeFolder}/spse/SPSENonTenderPengumuman{tahun}.parquet"
DatasetSPSENonTenderSelesai = f"https://storage.googleapis.com/bukanamel/{kodeFolder}/spse/SPSENonTenderSelesai{tahun}.parquet"
DatasetSPSENonTenderSPPBJ = f"https://storage.googleapis.com/bukanamel/{kodeFolder}/spse/SPSENonTenderEkontrakSPPBJ{tahun}.parquet"
DatasetSPSENonTenderKontrak = f"https://storage.googleapis.com/bukanamel/{kodeFolder}/spse/SPSENonTenderEkontrakKontrak{tahun}.parquet"
DatasetSPSENonTenderSPMK = f"https://storage.googleapis.com/bukanamel/{kodeFolder}/spse/SPSENonTenderEkontrakSPMKSPP{tahun}.parquet"
DatasetSPSENonTenderBAST = f"https://storage.googleapis.com/bukanamel/{kodeFolder}/spse/SPSENonTenderEkontrakBAPBAST{tahun}.parquet"

### Dataset Pencatatan
DatasetCatatNonTender = f"https://storage.googleapis.com/bukanamel/{kodeFolder}/spse/SPSEPencatatanNonTender{tahun}.parquet"
DatasetCatatNonTenderRealisasi = f"https://storage.googleapis.com/bukanamel/{kodeFolder}/spse/SPSEPencatatanNonTenderRealisasi{tahun}.parquet"
DatasetCatatSwakelola = f"https://storage.googleapis.com/bukanamel/{kodeFolder}/spse/SPSEPencatatanSwakelola{tahun}.parquet"
DatasetCatatSwakelolaRealisasi = f"https://storage.googleapis.com/bukanamel/{kodeFolder}/spse/SPSEPencatatanSwakelolaRealisasi{tahun}.parquet"

### Dataset Peserta Tender
DatasetPesertaTender = f"https://storage.googleapis.com/bukanamel/{kodeFolder}/spse/SPSEPesertaTender{tahun}.parquet"

### Dataset RUP Master Satker
DatasetRUPMasterSatker = f"https://storage.googleapis.com/bukanamel/{kodeFolder}/sirup/RUPMasterSatker{tahun}.parquet"

## Buat dataframe SPSE
### Baca file parquet dataset SPSE Tender
try:
    df_SPSETenderPengumuman = tarik_data(DatasetSPSETenderPengumuman)
except Exception:
    st.error("Gagal baca dataset SPSE Tender Pengumuman")
try:
    df_SPSETenderSelesai = tarik_data(DatasetSPSETenderSelesai)
except Exception:
    st.error("Gagal baca dataset SPSE Tender Selesai")
try:
    df_SPSETenderSelesaiNilai = tarik_data(DatasetSPSETenderSelesaiNilai)
except Exception:
    st.error("Gagal baca dataset SPSE Tender Selesai Nilai")
try:
    df_SPSETenderSPPBJ = tarik_data(DatasetSPSETenderSPPBJ)
except Exception:
    st.error("Gagal baca dataset SPSE Tender SPPBJ")    
try:    
    df_SPSETenderKontrak = tarik_data(DatasetSPSETenderKontrak)
except Exception:
    st.error("Gagal baca dataset SPSE Tender Kontrak")
try:
    df_SPSETenderSPMK = tarik_data(DatasetSPSETenderSPMK)
except Exception:
    st.error("Gagal baca dataset SPSE Tender SPMK")
try:
    df_SPSETenderBAST = tarik_data(DatasetSPSETenderBAST)
except Exception:
    st.error("Gagal baca dataset SPSE Tender BAST")

### Baca file parquet dataset SPSE Non Tender
try:
    df_SPSENonTenderPengumuman = tarik_data(DatasetSPSENonTenderPengumuman)
except Exception:
    st.error("Gagal baca dataset SPSE Non Tender Pengumuman")
try:
    df_SPSENonTenderSelesai = tarik_data(DatasetSPSENonTenderSelesai)
except Exception:
    st.error("Gagal baca dataset SPSE Non Tender Selesai")
try:
    df_SPSENonTenderSPPBJ = tarik_data(DatasetSPSENonTenderSPPBJ)
except Exception:
    st.error("Gagal baca dataset SPSE Non Tender SPPBJ")
try:
    df_SPSENonTenderKontrak = tarik_data(DatasetSPSENonTenderKontrak)
except Exception:
    st.error("Gagal baca dataset SPSE Non Tender Kontrak")
try:
    df_SPSENonTenderSPMK = tarik_data(DatasetSPSENonTenderSPMK)
except Exception:
    st.error("Gagal baca dataset SPSE Non Tender SPMK")
try:
    df_SPSENonTenderBAST = tarik_data(DatasetSPSENonTenderBAST)
except Exception:
    st.error("Gagal baca dataset SPSE Non Tender BAST")

### Baca file parquet dataset Pencatatan
try:
    df_CatatNonTender = tarik_data(DatasetCatatNonTender)
except Exception:
    st.error("Gagal baca dataset Catat Non Tender")
try:
    df_CatatNonTenderRealisasi = tarik_data(DatasetCatatNonTenderRealisasi)
except Exception:
    st.error("Gagal baca dataset Catat Non Tender Realisasi")
try:
    df_CatatSwakelola = tarik_data(DatasetCatatSwakelola)
except Exception:
    st.error("Gagal baca dataset Catat Swakelola")
try:
    df_CatatSwakelolaRealisasi = tarik_data(DatasetCatatSwakelolaRealisasi)
except Exception:
    st.error("Gagal baca dataset Catat Swakelola Realisasi")

### Baca file parquet dataset Peserta Tender
try:
    df_PesertaTender = tarik_data(DatasetPesertaTender)
except Exception:
    st.error("Gagal baca dataset Peserta Tender")

### Baca file parquet dataset RUP Master Satker
try:
    df_RUPMasterSatker = tarik_data(DatasetRUPMasterSatker)
except Exception:
    st.error("Gagal baca dataset RUP Master Satker")

#####
# Mulai membuat presentasi data SPSE
#####

# Buat menu yang mau disajikan
menu_spse_1, menu_spse_2, menu_spse_3, menu_spse_4 = st.tabs(["| TENDER |", "| NON TENDER |", "| PENCATATAN |", "| PESERTA TENDER |"])

## Tab menu SPSE - Tender
with menu_spse_1:

    st.header(f"SPSE - Tender - {pilih}")

    ### Buat sub menu SPSE - Tender
    menu_spse_1_1, menu_spse_1_2, menu_spse_1_3, menu_spse_1_4, menu_spse_1_5, menu_spse_1_6 = st.tabs(["| PENGUMUMAN |", "| SELESAI |", "| SPPBJ |", "| KONTRAK |", "| SPMK |", "| BAPBAST |"])

    #### Tab menu SPSE - Tender - Pengumuman
    with menu_spse_1_1:

        ##### Buat tombol unduh dataset SPSE-Tender-Pengumuman
        unduh_SPSE_Pengumuman = unduh_data(df_SPSETenderPengumuman)
        
        SPSE_Umumkan_1, SPSE_Umumkan_2 = st.columns((7,3))
        with SPSE_Umumkan_1:
            st.subheader("Pengumuman Tender")
        with SPSE_Umumkan_2:
            st.download_button(
                label = "📥 Download Data Pengumuman Tender",
                data = unduh_SPSE_Pengumuman,
                file_name = f"SPSETenderPengumuman-{kodeFolder}-{tahun}.csv",
                mime = "text/csv"
            )

        st.divider()

        SPSE_radio_1, SPSE_radio_2, SPSE_radio_3 = st.columns((1,1,8))
        with SPSE_radio_1:
            sumber_dana = st.radio("**Sumber Dana**", ["APBD", "APBDP", "BLUD"])
        with SPSE_radio_2:
            status_tender = st.radio("**Status Tender**", ["Selesai", "Gagal/Batal", "Berlangsung"])
        st.write(f"Anda memilih : **{sumber_dana}** dan **{status_tender}**")

        ##### Hitung-hitungan dataset Tender Pengumuman
        df_SPSETenderPengumuman_filter = con.execute(f"SELECT kd_tender, pagu, hps, kualifikasi_paket, jenis_pengadaan, mtd_pemilihan, mtd_evaluasi, mtd_kualifikasi, kontrak_pembayaran FROM df_SPSETenderPengumuman WHERE sumber_dana = '{sumber_dana}' AND status_tender = '{status_tender}' AND kualifikasi_paket IS NOT NULL").df()
        jumlah_trx_spse_pengumuman = df_SPSETenderPengumuman_filter['kd_tender'].unique().shape[0]
        nilai_trx_spse_pengumuman_pagu = df_SPSETenderPengumuman_filter['pagu'].sum()
        nilai_trx_spse_pengumuman_hps = df_SPSETenderPengumuman_filter['hps'].sum()

        data_umum_1, data_umum_2, data_umum_3 = st.columns(3)
        data_umum_1.metric(label="Jumlah Tender Diumumkan", value="{:,}".format(jumlah_trx_spse_pengumuman))
        data_umum_2.metric(label="Nilai Pagu Tender Diumumkan", value="{:,.2f}".format(nilai_trx_spse_pengumuman_pagu))
        data_umum_3.metric(label="Nilai HPS Tender Diumumkan", value="{:,.2f}".format(nilai_trx_spse_pengumuman_hps))
        style_metric_cards()

        st.divider()

        ####### Grafik jumlah dan nilai transaksi berdasarkan kualifikasi paket
        grafik_kp_1, grafik_kp_2 = st.tabs(["| Berdasarkan Jumlah Kualifikasi Paket |", "| Berdasarkan Nilai Kualifikasi Paket |"])

        with grafik_kp_1:

            st.subheader("Berdasarkan Jumlah Kualifikasi Paket")

            #### Query data grafik jumlah transaksi pengumuman SPSE berdasarkan kualifikasi paket

            sql_kp_jumlah = """
                SELECT kualifikasi_paket AS KUALIFIKASI_PAKET, COUNT(DISTINCT(kd_tender)) AS JUMLAH_PAKET
                FROM df_SPSETenderPengumuman_filter GROUP BY KUALIFIKASI_PAKET ORDER BY JUMLAH_PAKET DESC
            """
            
            tabel_kp_jumlah_trx = con.execute(sql_kp_jumlah).df()

            grafik_kp_1_1, grafik_kp_1_2 = st.columns((3,7))

            with grafik_kp_1_1:

                AgGrid(tabel_kp_jumlah_trx)

            with grafik_kp_1_2:

                st.bar_chart(tabel_kp_jumlah_trx, x="KUALIFIKASI_PAKET", y="JUMLAH_PAKET", color="KUALIFIKASI_PAKET")
    
        with grafik_kp_2:

            st.subheader("Berdasarkan Nilai Kualifikasi Paket")

            #### Query data grafik nilai transaksi pengumuman SPSE berdasarkan kualifikasi paket

            sql_kp_nilai = """
                SELECT kualifikasi_paket AS KUALIFIKASI_PAKET, SUM(pagu) AS NILAI_PAKET
                FROM df_SPSETenderPengumuman_filter GROUP BY KUALIFIKASI_PAKET ORDER BY NILAI_PAKET DESC
            """
            
            tabel_kp_nilai_trx = con.execute(sql_kp_nilai).df()

            grafik_kp_2_1, grafik_kp_2_2 = st.columns((3,7))

            with grafik_kp_2_1:

                gd = GridOptionsBuilder.from_dataframe(tabel_kp_nilai_trx)
                gd.configure_pagination()
                gd.configure_side_bar()
                gd.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True)
                gd.configure_column("NILAI_PAKET", type=["numericColumn", "numberColumnFilter", "customNumericFormat"], valueGetter = "data.NILAI_PAKET.toLocaleString('id-ID', {style: 'currency', currency: 'IDR', maximumFractionDigits:2})") 

                gridOptions = gd.build()
                AgGrid(tabel_kp_nilai_trx, gridOptions=gridOptions, enable_enterprise_modules=True)

            with grafik_kp_2_2:

                st.bar_chart(tabel_kp_nilai_trx, x="KUALIFIKASI_PAKET", y="NILAI_PAKET", color="KUALIFIKASI_PAKET")

        st.divider()

        ####### Grafik jumlah dan nilai transaksi berdasarkan Jenis Pengadaan
        grafik_jp_1, grafik_jp_2 = st.tabs(["| Berdasarkan Jumlah Jenis Pengadaan |", "| Berdasarkan Nilai Jenis Pengadaan |"])

        with grafik_jp_1:

            st.subheader("Berdasarkan Jumlah Jenis Pengadaan")

            #### Query data grafik jumlah transaksi pengumuman SPSE berdasarkan Jenis Pengadaan

            sql_jp_jumlah = """
                SELECT jenis_pengadaan AS JENIS_PENGADAAN, COUNT(DISTINCT(kd_tender)) AS JUMLAH_PAKET
                FROM df_SPSETenderPengumuman_filter GROUP BY JENIS_PENGADAAN ORDER BY JUMLAH_PAKET DESC
            """
            
            tabel_jp_jumlah_trx = con.execute(sql_jp_jumlah).df()

            grafik_jp_1_1, grafik_jp_1_2 = st.columns((3,7))

            with grafik_jp_1_1:

                AgGrid(tabel_jp_jumlah_trx)

            with grafik_jp_1_2:

                st.bar_chart(tabel_jp_jumlah_trx, x="JENIS_PENGADAAN", y="JUMLAH_PAKET", color="JENIS_PENGADAAN")
    
        with grafik_jp_2:

            st.subheader("Berdasarkan Nilai Jenis Pengadaan")

            #### Query data grafik nilai transaksi pengumuman SPSE berdasarkan Jenis Pengadaan

            sql_jp_nilai = """
                SELECT jenis_pengadaan AS JENIS_PENGADAAN, SUM(pagu) AS NILAI_PAKET
                FROM df_SPSETenderPengumuman_filter GROUP BY JENIS_PENGADAAN ORDER BY NILAI_PAKET DESC
            """
            
            tabel_jp_nilai_trx = con.execute(sql_jp_nilai).df()

            grafik_jp_2_1, grafik_jp_2_2 = st.columns((3,7))

            with grafik_jp_2_1:

                gd = GridOptionsBuilder.from_dataframe(tabel_jp_nilai_trx)
                gd.configure_pagination()
                gd.configure_side_bar()
                gd.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True)
                gd.configure_column("NILAI_PAKET", type=["numericColumn", "numberColumnFilter", "customNumericFormat"], valueGetter = "data.NILAI_PAKET.toLocaleString('id-ID', {style: 'currency', currency: 'IDR', maximumFractionDigits:2})") 

                gridOptions = gd.build()
                AgGrid(tabel_jp_nilai_trx, gridOptions=gridOptions, enable_enterprise_modules=True)

            with grafik_jp_2_2:

                st.bar_chart(tabel_jp_nilai_trx, x="JENIS_PENGADAAN", y="NILAI_PAKET", color="JENIS_PENGADAAN")

        st.divider()

        ####### Grafik jumlah dan nilai transaksi berdasarkan Metode Pemilihan
        grafik_mp_1, grafik_mp_2 = st.tabs(["| Berdasarkan Jumlah Metode Pemilihan |", "| Berdasarkan Nilai Metode Pemilihan |"])

        with grafik_mp_1:

            st.subheader("Berdasarkan Jumlah Metode Pemilihan")

            #### Query data grafik jumlah transaksi pengumuman SPSE berdasarkan Metode Pemilihan

            sql_mp_jumlah = """
                SELECT mtd_pemilihan AS METODE_PEMILIHAN, COUNT(DISTINCT(kd_tender)) AS JUMLAH_PAKET
                FROM df_SPSETenderPengumuman_filter GROUP BY METODE_PEMILIHAN ORDER BY JUMLAH_PAKET DESC
            """
            
            tabel_mp_jumlah_trx = con.execute(sql_mp_jumlah).df()

            grafik_mp_1_1, grafik_mp_1_2 = st.columns((3,7))

            with grafik_mp_1_1:

                AgGrid(tabel_mp_jumlah_trx)

            with grafik_mp_1_2:

                st.bar_chart(tabel_mp_jumlah_trx, x="METODE_PEMILIHAN", y="JUMLAH_PAKET", color="METODE_PEMILIHAN")
    
        with grafik_mp_2:

            st.subheader("Berdasarkan Nilai Metode Pemilihan")

            #### Query data grafik nilai transaksi pengumuman SPSE berdasarkan Metode Pemilihan

            sql_mp_nilai = """
                SELECT mtd_pemilihan AS METODE_PEMILIHAN, SUM(pagu) AS NILAI_PAKET
                FROM df_SPSETenderPengumuman_filter GROUP BY METODE_PEMILIHAN ORDER BY NILAI_PAKET DESC
            """
            
            tabel_mp_nilai_trx = con.execute(sql_mp_nilai).df()

            grafik_mp_2_1, grafik_mp_2_2 = st.columns((3,7))

            with grafik_mp_2_1:

                gd = GridOptionsBuilder.from_dataframe(tabel_mp_nilai_trx)
                gd.configure_pagination()
                gd.configure_side_bar()
                gd.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True)
                gd.configure_column("NILAI_PAKET", type=["numericColumn", "numberColumnFilter", "customNumericFormat"], valueGetter = "data.NILAI_PAKET.toLocaleString('id-ID', {style: 'currency', currency: 'IDR', maximumFractionDigits:2})") 

                gridOptions = gd.build()
                AgGrid(tabel_mp_nilai_trx, gridOptions=gridOptions, enable_enterprise_modules=True)

            with grafik_mp_2_2:

                st.bar_chart(tabel_mp_nilai_trx, x="METODE_PEMILIHAN", y="NILAI_PAKET", color="METODE_PEMILIHAN")

        st.divider()

        ####### Grafik jumlah dan nilai transaksi berdasarkan Metode Evaluasi
        grafik_me_1, grafik_me_2 = st.tabs(["| Berdasarkan Jumlah Metode Evaluasi |", "| Berdasarkan Nilai Metode Evaluasi |"])

        with grafik_me_1:

            st.subheader("Berdasarkan Jumlah Metode Evaluasi")

            #### Query data grafik jumlah transaksi pengumuman SPSE berdasarkan Metode Evaluasi

            sql_me_jumlah = """
                SELECT mtd_evaluasi AS METODE_EVALUASI, COUNT(DISTINCT(kd_tender)) AS JUMLAH_PAKET
                FROM df_SPSETenderPengumuman_filter GROUP BY METODE_EVALUASI ORDER BY JUMLAH_PAKET DESC
            """
            
            tabel_me_jumlah_trx = con.execute(sql_me_jumlah).df()

            grafik_me_1_1, grafik_me_1_2 = st.columns((3,7))

            with grafik_me_1_1:

                AgGrid(tabel_me_jumlah_trx)

            with grafik_me_1_2:

                st.bar_chart(tabel_me_jumlah_trx, x="METODE_EVALUASI", y="JUMLAH_PAKET", color="METODE_EVALUASI")
    
        with grafik_me_2:

            st.subheader("Berdasarkan Nilai Metode Evaluasi")

            #### Query data grafik nilai transaksi pengumuman SPSE berdasarkan Metode Evaluasi

            sql_me_nilai = """
                SELECT mtd_evaluasi AS METODE_EVALUASI, SUM(pagu) AS NILAI_PAKET
                FROM df_SPSETenderPengumuman_filter GROUP BY METODE_EVALUASI ORDER BY NILAI_PAKET DESC
            """
            
            tabel_me_nilai_trx = con.execute(sql_me_nilai).df()

            grafik_me_2_1, grafik_me_2_2 = st.columns((3,7))

            with grafik_me_2_1:

                gd = GridOptionsBuilder.from_dataframe(tabel_me_nilai_trx)
                gd.configure_pagination()
                gd.configure_side_bar()
                gd.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True)
                gd.configure_column("NILAI_PAKET", type=["numericColumn", "numberColumnFilter", "customNumericFormat"], valueGetter = "data.NILAI_PAKET.toLocaleString('id-ID', {style: 'currency', currency: 'IDR', maximumFractionDigits:2})") 

                gridOptions = gd.build()
                AgGrid(tabel_me_nilai_trx, gridOptions=gridOptions, enable_enterprise_modules=True)

            with grafik_me_2_2:

                st.bar_chart(tabel_me_nilai_trx, x="METODE_EVALUASI", y="NILAI_PAKET", color="METODE_EVALUASI")

        st.divider()

        ####### Grafik jumlah dan nilai transaksi berdasarkan Metode Kualifikasi
        grafik_mk_1, grafik_mk_2 = st.tabs(["| Berdasarkan Jumlah Metode Kualifikasi |", "| Berdasarkan Nilai Metode Kualifikasi |"])

        with grafik_mk_1:

            st.subheader("Berdasarkan Jumlah Metode Kualifikasi")

            #### Query data grafik jumlah transaksi pengumuman SPSE berdasarkan Metode Kualifikasi

            sql_mk_jumlah = """
                SELECT mtd_kualifikasi AS METODE_KUALIFIKASI, COUNT(DISTINCT(kd_tender)) AS JUMLAH_PAKET
                FROM df_SPSETenderPengumuman_filter GROUP BY METODE_KUALIFIKASI ORDER BY JUMLAH_PAKET DESC
            """
            
            tabel_mk_jumlah_trx = con.execute(sql_mk_jumlah).df()

            grafik_mk_1_1, grafik_mk_1_2 = st.columns((3,7))

            with grafik_mk_1_1:

                AgGrid(tabel_mk_jumlah_trx)

            with grafik_mk_1_2:

                st.bar_chart(tabel_mk_jumlah_trx, x="METODE_KUALIFIKASI", y="JUMLAH_PAKET", color="METODE_KUALIFIKASI")
    
        with grafik_mk_2:

            st.subheader("Berdasarkan Nilai Metode Kualifikasi")

            #### Query data grafik nilai transaksi pengumuman SPSE berdasarkan Metode Kualifikasi

            sql_mk_nilai = """
                SELECT mtd_kualifikasi AS METODE_KUALIFIKASI, SUM(pagu) AS NILAI_PAKET
                FROM df_SPSETenderPengumuman_filter GROUP BY METODE_KUALIFIKASI ORDER BY NILAI_PAKET DESC
            """
            
            tabel_mk_nilai_trx = con.execute(sql_mk_nilai).df()

            grafik_mk_2_1, grafik_mk_2_2 = st.columns((3,7))

            with grafik_mk_2_1:

                gd = GridOptionsBuilder.from_dataframe(tabel_mk_nilai_trx)
                gd.configure_pagination()
                gd.configure_side_bar()
                gd.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True)
                gd.configure_column("NILAI_PAKET", type=["numericColumn", "numberColumnFilter", "customNumericFormat"], valueGetter = "data.NILAI_PAKET.toLocaleString('id-ID', {style: 'currency', currency: 'IDR', maximumFractionDigits:2})") 

                gridOptions = gd.build()
                AgGrid(tabel_mk_nilai_trx, gridOptions=gridOptions, enable_enterprise_modules=True)

            with grafik_mk_2_2:

                st.bar_chart(tabel_mk_nilai_trx, x="METODE_KUALIFIKASI", y="NILAI_PAKET", color="METODE_KUALIFIKASI")

        st.divider()

        ####### Grafik jumlah dan nilai transaksi berdasarkan Kontrak Pembayaran
        grafik_kontrak_1, grafik_kontrak_2 = st.tabs(["| Berdasarkan Jumlah Kontrak Pembayaran |", "| Berdasarkan Nilai Kontrak Pembayaran |"])

        with grafik_kontrak_1:

            st.subheader("Berdasarkan Jumlah Kontrak Pembayaran")

            #### Query data grafik jumlah transaksi pengumuman SPSE berdasarkan Kontrak Pembayaran

            sql_kontrak_jumlah = """
                SELECT kontrak_pembayaran AS KONTRAK_PEMBAYARAN, COUNT(DISTINCT(kd_tender)) AS JUMLAH_PAKET
                FROM df_SPSETenderPengumuman_filter GROUP BY KONTRAK_PEMBAYARAN ORDER BY JUMLAH_PAKET DESC
            """
            
            tabel_kontrak_jumlah_trx = con.execute(sql_kontrak_jumlah).df()

            grafik_kontrak_1_1, grafik_kontrak_1_2 = st.columns((3,7))

            with grafik_kontrak_1_1:

                AgGrid(tabel_kontrak_jumlah_trx)

            with grafik_kontrak_1_2:

                st.bar_chart(tabel_kontrak_jumlah_trx, x="KONTRAK_PEMBAYARAN", y="JUMLAH_PAKET", color="KONTRAK_PEMBAYARAN")
    
        with grafik_kontrak_2:

            st.subheader("Berdasarkan Nilai Kontrak Pembayaran")

            #### Query data grafik nilai transaksi pengumuman SPSE berdasarkan Kontrak Pembayaran

            sql_kontrak_nilai = """
                SELECT kontrak_pembayaran AS KONTRAK_PEMBAYARAN, SUM(pagu) AS NILAI_PAKET
                FROM df_SPSETenderPengumuman_filter GROUP BY KONTRAK_PEMBAYARAN ORDER BY NILAI_PAKET DESC
            """
            
            tabel_kontrak_nilai_trx = con.execute(sql_kontrak_nilai).df()

            grafik_kontrak_2_1, grafik_kontrak_2_2 = st.columns((3,7))

            with grafik_kontrak_2_1:

                gd = GridOptionsBuilder.from_dataframe(tabel_kontrak_nilai_trx)
                gd.configure_pagination()
                gd.configure_side_bar()
                gd.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True)
                gd.configure_column("NILAI_PAKET", type=["numericColumn", "numberColumnFilter", "customNumericFormat"], valueGetter = "data.NILAI_PAKET.toLocaleString('id-ID', {style: 'currency', currency: 'IDR', maximumFractionDigits:2})") 

                gridOptions = gd.build()
                AgGrid(tabel_kontrak_nilai_trx, gridOptions=gridOptions, enable_enterprise_modules=True)

            with grafik_kontrak_2_2:

                st.bar_chart(tabel_kontrak_nilai_trx, x="KONTRAK_PEMBAYARAN", y="NILAI_PAKET", color="KONTRAK_PEMBAYARAN")

        st.divider()

    #### Tab menu SPSE - Tender - Selesai
    with menu_spse_1_2:
        
        st.subheader("SPSE-Tender-Selesai")

    #### Tab menu SPSE - Tender - SPPBJ
    with menu_spse_1_3:

        ##### Buat tombol unduh dataset SPSE-Tender-SPPBJ
        unduh_SPSE_Tender_SPPBJ = unduh_data(df_SPSETenderSPPBJ)

        SPSE_SPPBJ_1, SPSE_SPPBJ_2 = st.columns((7,3))
        with SPSE_SPPBJ_1:
            st.subheader("SPSE-Tender-SPPBJ")
        with SPSE_SPPBJ_2:
            st.download_button(
                label = "📥 Download Data Tender SPPBJ",
                data = unduh_SPSE_Tender_SPPBJ,
                file_name = f"SPSETenderSPPBJ-{kodeFolder}-{tahun}.csv",
                mime = "text/csv"
            )

        st.divider()

        SPSE_SPPBJ_radio_1, SPSE_SPPBJ_radio_2 = st.columns((2,8))
        with SPSE_SPPBJ_radio_1:
            status_kontrak = st.radio("**Status Kontrak**", ["Kontrak Selesai", "Kontrak Sedang Berjalan"])
        with SPSE_SPPBJ_radio_2:
            opd = st.selectbox("Pilih Perangkat Daerah :", df_SPSETenderSPPBJ['nama_satker'].unique(), key='opd_sppbj')
        st.write(f"Anda memilih : **{status_kontrak}** dari **{opd}**")

        ##### Hitung-hitungan dataset SPSE-Tender-SPPBJ
        df_SPSETenderSPPBJ_filter = con.execute(f"SELECT * FROM df_SPSETenderSPPBJ WHERE status_kontrak = '{status_kontrak}' AND nama_satker = '{opd}'").df()
        jumlah_trx_spse_sppbj = df_SPSETenderSPPBJ_filter['kd_tender'].unique().shape[0]
        nilai_trx_spse_sppbj_final = df_SPSETenderSPPBJ_filter['harga_final'].sum()

        data_sppbj_1, data_sppbj_2 = st.columns(2)
        data_sppbj_1.metric(label="Jumlah Tender SPPBJ", value="{:,}".format(jumlah_trx_spse_sppbj))
        data_sppbj_2.metric(label="Nilai Tender SPPBJ", value="{:,.2f}".format(nilai_trx_spse_sppbj_final))
        style_metric_cards()

        st.divider()
        
        sql_query_sppbj_tbl = """
            SELECT nama_paket AS NAMA_PAKET, no_sppbj AS NO_SPPBJ, tgl_sppbj AS TGL_SPPBJ, 
            nama_ppk AS NAMA_PPK, nama_penyedia AS NAMA_PENYEDIA, npwp_penyedia AS NPWP_PENYEDIA, 
            harga_final AS HARGA_FINAL FROM df_SPSETenderSPPBJ_filter
        """
        df_SPSETenderSPPBJ_tbl_tampil = con.execute(sql_query_sppbj_tbl).df()

        ##### Tampilkan data SPSE Tender SPPBJ menggunakan AgGrid
        gd = GridOptionsBuilder.from_dataframe(df_SPSETenderSPPBJ_tbl_tampil)
        gd.configure_pagination()
        gd.configure_side_bar()
        gd.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True)
        gd.configure_column("HARGA_FINAL", type=["numericColumn", "numberColumnFilter", "customNumericFormat"], valueGetter = "data.HARGA_FINAL.toLocaleString('id-ID', {style: 'currency', currency: 'IDR', maximumFractionDigits:2})")

        gridOptions = gd.build()
        AgGrid(df_SPSETenderSPPBJ_tbl_tampil, gridOptions=gridOptions, enable_enterprise_modules=True) 


    #### Tab menu SPSE - Tender - Kontrak
    with menu_spse_1_4:

        st.subheader("SPSE-Tender-Kontrak")

    #### Tab menu SPSE - Tender - SPMK
    with menu_spse_1_5:

        st.subheader("SPSE-Tender-SPMK")

    #### Tab menu SPSE - Tender - BAPBAST
    with menu_spse_1_6:

        st.subheader("SPSE-Tender-BAPBAST")

## Tab menu SPSE - Non Tender
with menu_spse_2:

    st.header("SPSE - Non Tender")

## Tab menu SPSE - Pencatatan
with menu_spse_3:

    st.header(f"SPSE - Pencatatan Transaksi PBJ - {pilih}")

    ### Buat sub menu SPSE - Pencatatan Transaksi PBJ
    menu_spse_3_1, menu_spse_3_2 = st.tabs(["| Pencatatan Non Tender |", "| Pencatatan Swakelola |"])

    #### Query penggabungan dataset CatatNonTender dan CatatSwakelola
    df_CatatNonTenderRealisasi_Filter = ""
    df_CatatNonTender_OK = ""

    df_CatatSwakelolaRealisasi_filter = df_CatatSwakelolaRealisasi[["kd_swakelola_pct", "jenis_realisasi", "no_realisasi", "tgl_realisasi", "nilai_realisasi"]] 
    df_CatatSwakelola_OK = df_CatatSwakelola.merge(df_CatatSwakelolaRealisasi_filter, how='left', on='kd_swakelola_pct')
    
    #### Tab menu SPSE - Pencatatan - Non Tender
    with menu_spse_3_1:

        #### Buat tombol unduh dataset SPSE-Pencatatan-Non Tender
        unduh_CATAT_NonTender = unduh_data(df_CatatNonTender)

        SPSE_CATAT_NonTender_1, SPSE_CATAT_NonTender_2 = st.columns((7,3))
        with SPSE_CATAT_NonTender_1:
            st.subheader("Pencatatan Non Tender")
        with SPSE_CATAT_NonTender_2:
            st.download_button(
                label = "📥 Download Data Pencatatan Non Tender",
                data = unduh_CATAT_NonTender,
                file_name = f"SPSEPencatatanNonTender-{kodeFolder}-{tahun}.csv",
                mime = "text/csv"
            )

        st.divider()

    #### Tab menu SPSE - Pencatatan - Swakelola
    with menu_spse_3_2:

        #### Buat tombol unduh dataset SPSE-Pencatatan-Swakelola
        unduh_CATAT_Swakelola = unduh_data(df_CatatSwakelola_OK)

        SPSE_CATAT_Swakelola_1, SPSE_CATAT_Swakelola_2 = st.columns((7,3))
        with SPSE_CATAT_Swakelola_1:
            st.subheader("Pencatatan Swakelola")
        with SPSE_CATAT_Swakelola_2:
            st.download_button(
                label = "📥 Download Data Pencatatan Swakelola",
                data = unduh_CATAT_Swakelola,
                file_name = f"SPSEPencatatanSwakelola-{kodeFolder}-{tahun}.csv",
                mime = "text/csv"
            )

        st.divider()

        sumber_dana_cs = st.radio("**Sumber Dana :**", df_CatatSwakelola_OK['sumber_dana'].unique(), key="CatatSwakelola")
        st.write(f"Anda memilih : **{sumber_dana_cs}**")

        #### Hitung-hitungan dataset Catat Swakelola
        df_CatatSwakelola_OK_filter = con.execute(f"SELECT * FROM df_CatatSwakelola_OK WHERE sumber_dana = '{sumber_dana_cs}'").df()
        jumlah_CatatSwakelola_Berjalan = con.execute(f"SELECT * FROM df_CatatSwakelola_OK_filter WHERE status_swakelola_pct_ket = 'Paket Sedang Berjalan'").df()
        jumlah_CatatSwakelola_Selesai = con.execute(f"SELECT * FROM df_CatatSwakelola_OK_filter WHERE status_swakelola_pct_ket = 'Paket Selesai'").df()
        jumlah_CatatSwakelola_dibatalkan = con.execute(f"SELECT * FROM df_CatatSwakelola_OK_filter WHERE status_swakelola_pct_ket = 'Paket Dibatalkan'").df()

        data_cs_1, data_cs_2, data_cs_3 = st.columns(3)
        data_cs_1.metric(label="Jumlah Pencatatan Swakelola Berjalan", value="{:,}".format(jumlah_CatatSwakelola_Berjalan.shape[0]))
        data_cs_2.metric(label="Jumlah Pencacatan Swakelola Selesai", value="{:,}".format(jumlah_CatatSwakelola_Selesai.shape[0]))
        data_cs_3.metric(label="Jumlah Pencatatan Swakelola Dibatalkan", value="{:,}".format(jumlah_CatatSwakelola_dibatalkan.shape[0]))
        style_metric_cards()

        st.divider()

        status_swakelola_cs = st.radio("**Status Swakelola :**", df_CatatSwakelola_OK_filter['status_swakelola_pct_ket'].unique())
        status_opd_cs = st.selectbox("**Pilih Satker :**", df_CatatSwakelola_OK_filter['nama_satker'].unique())

        df_CatatSwakelola_tabel = con.execute(f"SELECT nama_paket AS NAMA_PAKET, jenis_realisasi AS JENIS_REALISASI, no_realisasi AS NO_REALISASI, tgl_realisasi AS TGL_REALISASI, pagu AS PAGU, total_realisasi AS TOTAL_REALISASI, nilai_realisasi AS NILAI_REALISASI, nama_ppk AS NAMA_PPK FROM df_CatatSwakelola_OK_filter WHERE nama_satker = '{status_opd_cs}' AND status_swakelola_pct_ket = '{status_swakelola_cs}'").df()

        gd = GridOptionsBuilder.from_dataframe(df_CatatSwakelola_tabel)
        gd.configure_pagination()
        gd.configure_side_bar()
        gd.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True)
        gd.configure_column("PAGU", type=["numericColumn", "numberColumnFilter", "customNumericFormat"], valueGetter = "data.PAGU.toLocaleString('id-ID', {style: 'currency', currency: 'IDR', maximumFractionDigits:2})")
        gd.configure_column("TOTAL_REALISASI", type=["numericColumn", "numberColumnFilter", "customNumericFormat"], valueGetter = "data.TOTAL_REALISASI.toLocaleString('id-ID', {style: 'currency', currency: 'IDR', maximumFractionDigits:2})")
        gd.configure_column("NILAI_REALISASI", type=["numericColumn", "numberColumnFilter", "customNumericFormat"], valueGetter = "data.NILAI_REALISASI.toLocaleString('id-ID', {style: 'currency', currency: 'IDR', maximumFractionDigits:2})")
        
        gridOptions = gd.build()
        AgGrid(df_CatatSwakelola_tabel, gridOptions=gridOptions, enable_enterprise_modules=True)

## Tab menu SPSE - Peserta Tender
with menu_spse_4:

    ### Persiapan dataset Peserta Tender vs Master Satker

    #### Query penggabungan dataset Peserta Tender vs Master Satker

    sql_query_PesertaTenderDetail_1 = """
        SELECT nama_satker, nama_penyedia, npwp_penyedia, nilai_penawaran, nilai_terkoreksi, pemenang, pemenang_terverifikasi, kd_tender
        FROM df_PesertaTender, df_RUPMasterSatker 
        WHERE df_PesertaTender.kd_satker_str = df_RUPMasterSatker.kd_satker_str 
    """

    sql_query_PesertaTenderDetail_2 = """
        SELECT df_PesertaTenderDetail_1.nama_satker, df_SPSETenderPengumuman.nama_paket, df_SPSETenderPengumuman.pagu, df_SPSETenderPengumuman.hps, df_SPSETenderPengumuman.sumber_dana, df_PesertaTenderDetail_1.nama_penyedia, df_PesertaTenderDetail_1.npwp_penyedia, df_PesertaTenderDetail_1.nilai_penawaran, df_PesertaTenderDetail_1.nilai_terkoreksi, df_PesertaTenderDetail_1.pemenang, df_PesertaTenderDetail_1.pemenang_terverifikasi
        FROM df_PesertaTenderDetail_1, df_SPSETenderPengumuman 
        WHERE df_PesertaTenderDetail_1.kd_tender = df_SPSETenderPengumuman.kd_tender
    """

    df_PesertaTenderDetail_1 = con.execute(sql_query_PesertaTenderDetail_1).df()
    df_PesertaTenderDetail_2 = con.execute(sql_query_PesertaTenderDetail_2).df()

    #### Buat tombol unduh dataset Peserta Tender
    unduh_Peserta_Tender = unduh_data(df_PesertaTenderDetail_2)

    SPSE_PT_D_1, SPSE_PT_D_2 = st.columns((7,2))
    with SPSE_PT_D_1:
        st.header(f"SPSE - Peserta Tender - {pilih}")
    with SPSE_PT_D_2:
        st.download_button(
            label = "📥 Download Data Peserta Tender",
            data = unduh_Peserta_Tender,
            file_name = f"SPSEPesertaTenderDetail-{kodeFolder}-{tahun}.csv",
            mime = "text/csc"
        )

    st.divider()

    sumber_dana_pt = st.radio("**Sumber Dana :**", ["APBD", "APBDP", "BLUD"], key="PesertaTender")
    st.write(f"Anda memilih : **{sumber_dana_pt}**")

    #### Hitung-hitungan dataset Peserta Tender
    df_PesertaTenderDetail_filter = con.execute(f"SELECT * FROM df_PesertaTenderDetail_2 WHERE sumber_dana = '{sumber_dana_pt}' AND nama_penyedia IS NOT NULL").df()
    jumlah_PesertaTender_daftar = con.execute(f"SELECT * FROM df_PesertaTenderDetail_filter WHERE nilai_penawaran = 0 AND nilai_terkoreksi = 0").df()
    jumlah_PesertaTender_nawar = con.execute(f"SELECT * FROM df_PesertaTenderDetail_filter WHERE nilai_penawaran != 0 AND nilai_terkoreksi != 0").df()
    jumlah_PesertaTender_menang = con.execute(f"SELECT * FROM df_PesertaTenderDetail_filter WHERE pemenang != 0").df()

    data_pt_1, data_pt_2, data_pt_3 = st.columns(3)
    data_pt_1.metric(label="Jumlah Peserta Yang Mendaftar", value="{:,}".format(jumlah_PesertaTender_daftar['nama_penyedia'].shape[0]))
    data_pt_2.metric(label="Jumlah Peserta Yang Menawar", value="{:,}".format(jumlah_PesertaTender_nawar['nama_penyedia'].shape[0]))
    data_pt_3.metric(label="Jumlah Peserta Yang Menang", value="{:,}".format(jumlah_PesertaTender_menang.shape[0]))
    style_metric_cards()

    st.divider()

    opd_pt = df_PesertaTenderDetail_filter['nama_satker'].unique()
    status_pemenang_pt = st.radio("**Tabel Data Peserta :**", ["PEMENANG", "MENDAFTAR", "MENAWAR"])
    status_opd_pt = st.selectbox("**Pilih Satker :**", opd_pt)

    if status_pemenang_pt == "PEMENANG":
        jumlah_PeserteTender = con.execute(f"SELECT nama_paket, nama_penyedia, npwp_penyedia, pagu, hps, nilai_penawaran, nilai_terkoreksi FROM df_PesertaTenderDetail_filter WHERE nama_satker = '{status_opd_pt}' AND pemenang != 0").df()
    elif status_pemenang_pt == "MENDAFTAR":
        jumlah_PeserteTender = con.execute(f"SELECT nama_paket, nama_penyedia, npwp_penyedia, pagu, hps, nilai_penawaran, nilai_terkoreksi FROM df_PesertaTenderDetail_filter WHERE nama_satker = '{status_opd_pt}' AND nilai_penawaran = 0 AND nilai_terkoreksi = 0").df()
    else:
        jumlah_PeserteTender = con.execute(f"SELECT nama_paket, nama_penyedia, npwp_penyedia, pagu, hps, nilai_penawaran, nilai_terkoreksi FROM df_PesertaTenderDetail_filter WHERE nama_satker = '{status_opd_pt}' AND nilai_penawaran != 0 AND nilai_terkoreksi != 0").df()

    gd = GridOptionsBuilder.from_dataframe(jumlah_PeserteTender)
    gd.configure_pagination()
    gd.configure_side_bar()
    gd.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True)
    gd.configure_column("pagu", type=["numericColumn", "numberColumnFilter", "customNumericFormat"], valueGetter = "data.pagu.toLocaleString('id-ID', {style: 'currency', currency: 'IDR', maximumFractionDigits:2})")
    gd.configure_column("hps", type=["numericColumn", "numberColumnFilter", "customNumericFormat"], valueGetter = "data.hps.toLocaleString('id-ID', {style: 'currency', currency: 'IDR', maximumFractionDigits:2})")
    gd.configure_column("nilai_penawaran", type=["numericColumn", "numberColumnFilter", "customNumericFormat"], valueGetter = "data.nilai_penawaran.toLocaleString('id-ID', {style: 'currency', currency: 'IDR', maximumFractionDigits:2})")
    gd.configure_column("nilai_terkoreksi", type=["numericColumn", "numberColumnFilter", "customNumericFormat"], valueGetter = "data.nilai_terkoreksi.toLocaleString('id-ID', {style: 'currency', currency: 'IDR', maximumFractionDigits:2})")
    
    gridOptions = gd.build()
    AgGrid(jumlah_PeserteTender, gridOptions=gridOptions, enable_enterprise_modules=True)
