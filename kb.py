import random
import datetime

# Struktur Data: List untuk menyimpan tugas
tasks = []

def add_task():
    """Menambahkan tugas baru"""
    task_name = input("Masukkan nama tugas: ")
    deadline = input("Masukkan deadline (YYYY-MM-DD): ")
    task_id = random.randint(1000, 9999)  # ID unik untuk setiap tugas
    
    task = {
        "id": task_id,
        "name": task_name,
        "deadline": deadline,
        "added_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    tasks.append(task)
    print(f"Tugas '{task_name}' berhasil ditambahkan dengan ID {task_id}!\n")

def show_tasks():
    """Menampilkan semua tugas"""
    if not tasks:
        print("Belum ada tugas yang ditambahkan.\n")
        return
    
    print("Daftar Tugas:")
    for task in tasks:
        print(f"[ID: {task['id']}] {task['name']} - Deadline: {task['deadline']} (Ditambahkan: {task['added_at']})")
    print()

def delete_task():
    """Menghapus tugas berdasarkan ID"""
    show_tasks()
    try:
        task_id = int(input("Masukkan ID tugas yang ingin dihapus: "))
        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                print(f"Tugas '{task['name']}' berhasil dihapus!\n")
                return
        print("ID tidak ditemukan!\n")
    except ValueError:
        print("Masukkan ID yang valid!\n")

def main():
    """Menu utama"""
    while True:
        print("\n=== SISTEM MANAJEMEN TUGAS ===")
        print("1. Tambah Tugas")
        print("2. Lihat Tugas")
        print("3. Hapus Tugas")
        print("4. Keluar")
        
        choice = input("Pilih menu: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Terima kasih! Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, coba lagi!\n")

if __name__ == "__main__":
    main()
