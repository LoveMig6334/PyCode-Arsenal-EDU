import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress


def analyze_gravity(filename):
    """
    ฟังก์ชันสำหรับอ่านไฟล์ วิเคราะห์ค่า G และพลอตกราฟ
    """
    try:
        # 1. อ่านไฟล์ข้อมูล
        # skiprows=1 เพราะบรรทัดแรกเป็น metadata (;mass A;;)
        # sep=';' ระบุว่าใช้เครื่องหมาย ; ในการคั่นข้อมูล
        df = pd.read_csv(filename, sep=";", skiprows=1)

        # ลบคอลัมน์ที่ไม่มีข้อมูล (เนื่องจากในไฟล์อาจมี ; ปิดท้ายแถว ทำให้เกิดคอลัมน์ว่าง)
        df = df.dropna(axis=1, how="all")

        # ตรวจสอบว่ามีคอลัมน์ t และ y หรือไม่
        if "t" not in df.columns or "y" not in df.columns:
            # พยายามลบช่องว่างในชื่อคอลัมน์ (เช่น ' t' -> 't')
            df.columns = df.columns.str.strip()

        # ดึงค่า t และ y ออกมาเป็นตัวแปร array
        t = df["t"].values
        y = df["y"].values

        # 2. คำนวณความเร็ว (Velocity)
        # ใช้ np.gradient เพื่อหาอนุพันธ์ dy/dt (ความชันของกราฟ y-t ณ จุดนั้นๆ)
        v = np.gradient(y, t)

        # 3. คำนวณหาค่า G (ความชันของกราฟ v-t) ด้วย Linear Regression
        slope, intercept, r_value, p_value, std_err = linregress(t, v)

        # ค่าความเร่งที่คำนวณได้ (G) คือความชันของกราฟ
        calculated_g = slope
        r_squared = r_value**2

        print("--------------------------------------------------")
        print(f"ผลการวิเคราะห์ข้อมูลจากไฟล์: {filename}")
        print("--------------------------------------------------")
        print(f"สมการความเร็ว: v = {slope:.4f}t + {intercept:.4f}")
        print(f"ค่าความเร่ง (G) ที่คำนวณได้: {abs(calculated_g):.4f} m/s^2")
        print(f"ค่า R-squared (ความแม่นยำของการฟิตกราฟ): {r_squared:.4f}")
        print("--------------------------------------------------")

        # 4. การแสดงผลกราฟ
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10), sharex=True)

        # กราฟที่ 1: การกระจัด (y) เทียบกับ เวลา (t)
        ax1.plot(t, y, "b.", label="Position Data")
        ax1.set_ylabel("Position y (m)", fontsize=12)
        ax1.set_title("Free Fall: Position vs Time", fontsize=14)
        ax1.grid(True, linestyle="--", alpha=0.6)
        ax1.legend()

        # กราฟที่ 2: ความเร็ว (v) เทียบกับ เวลา (t)
        ax2.plot(t, v, "r.", label="Calculated Velocity", alpha=0.5)

        # สร้างเส้น Linear Regression เพื่อแสดงแนวโน้ม
        v_fit = slope * t + intercept
        ax2.plot(
            t, v_fit, "k-", linewidth=2, label=f"Linear Fit (Slope/G = {slope:.2f})"
        )

        ax2.set_xlabel("Time t (s)", fontsize=12)
        ax2.set_ylabel("Velocity v (m/s)", fontsize=12)
        ax2.set_title("Free Fall: Velocity vs Time", fontsize=14)
        ax2.grid(True, linestyle="--", alpha=0.6)

        # ใส่กล่องข้อความแสดงผลลัพธ์บนกราฟ
        textstr = "\n".join(
            (
                f"Calculated G = {abs(calculated_g):.3f} $m/s^2$",
                f"$R^2$ = {r_squared:.4f}",
                f"Eq: $v = {slope:.2f}t + {intercept:.2f}$",
            )
        )
        props = dict(boxstyle="round", facecolor="wheat", alpha=0.5)
        ax2.text(
            0.05,
            0.95,
            textstr,
            transform=ax2.transAxes,
            fontsize=11,
            verticalalignment="top",
            bbox=props,
        )

        ax2.legend(loc="lower left")

        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print(
            f"Error: ไม่พบไฟล์ '{filename}' กรุณาตรวจสอบว่าไฟล์วางอยู่โฟลเดอร์เดียวกับ script หรือไม่"
        )
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # เรียกใช้งานฟังก์ชัน โดยส่งชื่อไฟล์ข้อมูลเข้าไป
    # ใช้ os.path เพื่อระบุ path ของไฟล์ให้ถูกต้อง ไม่ว่าจะ run จาก folder ไหน
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "masos.txt")
    analyze_gravity(file_path)
