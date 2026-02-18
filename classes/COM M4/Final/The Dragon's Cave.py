import random
import time

treasure_log = []
game_history = []


def revive_input(mag, in_choice) -> int:
    while True:
        try:
            choice = int(input(mag))

            if choice in in_choice:
                return choice
            else:
                print("กรอกตัวเลือกที่มีอยู่เท่านั้น")
                continue

        except ValueError:
            print("กรอกตัวเลข เท่านั้น")
            continue


def cal_score(lvl: int) -> int:
    return 100 * (2**lvl)


def clear_screen() -> None:
    for i in range(4):
        print()


def game() -> None:
    print("ยินดีต้อนรับสู่เกมพิชิตถ้ำมังกร The Dragon's Cave")
    lvl = 0

    while True:
        print(f"ด่านที่ {lvl + 1} จงเสี่ยงโชคเลือกทางที่ถูก")

        print("ซ้าย กด 1")
        print("ขวา กด 2")
        print("ออกจากถ้ำ กด 3")

        player_chi = revive_input("กรอกตัวเลือก: ", [1, 2, 3])
        have_dragon = random.randint(1, 2)

        if player_chi == have_dragon:
            print("มีมังกร ตายห้า ไปเริ่มไหม่นะ")
            time.sleep(1)
            break

        elif player_chi == 3:
            print("ไว้เจอกันนะ")
            game_history.append(sum(treasure_log))
            lvl = 0
            break

        else:
            print()
            print("รอด ไปด่านต่อไป")
            print()
            treasure_log.append(cal_score(lvl))
            lvl += 1


def menu() -> None:
    while True:
        print("ยินดีต้อนรับสู่เกมพิชิตถ้ำมังกร The Dragon's Cave")
        print("ออกจากโปรแกรม กด 999")
        print("ดูสถิติการเล่น กด 888")
        print("เข้าเล่นเกม กด 777")
        menu_c = revive_input("กรอกตัวเลือก: ", [999, 888, 777])

        if menu_c == 999:
            print("End the program")
            break
        elif menu_c == 888:
            game_history.sort(reverse=True)

            if game_history == []:
                print("ยังไม่มีสถิติการเล่น")
                print()
            else:
                print()
                print("สถิติการเล่น")
                for i in range(len(game_history)):
                    print(f"{i + 1} : {game_history[i]}")
                print()
        else:
            clear_screen()
            game()
            clear_screen()


if __name__ == "__main__":
    menu()
