import random

VALID_BETS = (10, 20, 50, 100)
INITIAL_BALANCE = 500
COMMISSION_RATE = 0.10
VIEW_STATS_CODE = 88
EXIT_CODE = 99


def start_game() -> dict:
    print("IREM 888 | เกมปั่นแปะ")
    print(f"เงินเดิมพันเริ่มต้น: {INITIAL_BALANCE} บาท")
    print(f"ตัวเลือกเดิมพัน: {VALID_BETS} บาท")
    print(f"พิมพ์ {VIEW_STATS_CODE} เพื่อดูสถิติ")
    print(f"พิมพ์ {EXIT_CODE} เพื่อออกจากเกม")
    print("=" * 50)

    return {
        "balance": INITIAL_BALANCE,
        "rounds_played": 0,
        "wins": 0,
        "losses": 0,
        "history": [],  # List to store game history
    }


def get_bet(balance: int) -> int:
    while True:
        print(f"\nเงินคงเหลือ: {balance} บาท")
        print(f"เลือกจำนวนเงินเดิมพัน {VALID_BETS} บาท")
        print(f"หรือพิมพ์ {VIEW_STATS_CODE} ดูสถิติ / {EXIT_CODE} ออกจากเกม")

        try:
            choice = int(input("ใส่จำนวนเงิน: "))

            # Check for special codes
            if choice == VIEW_STATS_CODE:
                return VIEW_STATS_CODE
            elif choice == EXIT_CODE:
                return EXIT_CODE

            # Validate bet amount
            if choice not in VALID_BETS:
                print(f"กรุณาเลือกเดิมพัน {VALID_BETS} บาท เท่านั้น!")
                continue

            if choice > balance:
                print("เงินไม่พอ! กรุณาเลือกจำนวนเงินที่น้อยกว่า")
                continue

            return choice

        except ValueError:
            print("กรุณาใส่ตัวเลขเท่านั้น!")


def get_guess() -> str:
    choices = {"1": "หัว", "2": "ก้อย"}

    while True:
        print("\nเลือกทาย:")
        print("1. หัว (Heads)")
        print("2. ก้อย (Tails)")

        choice = input("เลือก (1 หรือ 2): ").strip()

        if choice in choices:
            return choices[choice]
        else:
            print("กรุณาเลือก 1 หรือ 2 เท่านั้น!")


def flip_coin(player_guess=None) -> str:
    if player_guess is None:
        return "หัว" if random.randint(0, 1) == 0 else "ก้อย"
    else:
        return "หัว" if player_guess == "ก้อย" else "ก้อย"


def calculate_win(bet_amount: int) -> int:
    base_win = bet_amount * 2
    commission = base_win * COMMISSION_RATE
    total_win = base_win + commission
    return total_win


def play_round(game_state, bet_amount, player_guess) -> None:
    """Play a single round and update game state."""
    coin_result = flip_coin(player_guess)

    print(f"\n🪙 ผลคือ: {coin_result}!")

    # Check if player won
    if player_guess == coin_result:
        winnings = calculate_win(bet_amount)
        game_state["balance"] += winnings - bet_amount  # Net gain
        game_state["wins"] += 1
        result = "win"
        print("✅ ยินดีด้วย! คุณทายถูก!")
        print(f"💰 ได้รับ: {winnings:.2f} บาท (เดิมพัน x2 + 10% commission)")
    else:
        game_state["balance"] -= bet_amount
        game_state["losses"] += 1
        result = "lose"
        print("❌ เสียใจด้วย! คุณทายผิด")
        print(f"💸 เสียเงิน: {bet_amount} บาท")

    print("=" * 50)
    game_state["rounds_played"] += 1

    # Store in history (list of tuples)
    game_state["history"].append(
        (game_state["rounds_played"], bet_amount, player_guess, coin_result, result)
    )

    return game_state


def display_statistics(game_state):
    """Display game statistics."""
    print("\n" + "=" * 50)
    print("📊 สถิติการเล่น")

    stats = [
        f"เงินคงเหลือ: {game_state['balance']:.2f} บาท",
        f"จำนวนรอบที่เล่น: {game_state['rounds_played']} รอบ",
        f"จำนวนรอบที่ชนะ: {game_state['wins']} รอบ",
        f"จำนวนรอบที่แพ้: {game_state['losses']} รอบ",
    ]

    for stat in stats:
        print(stat)

    # Calculate win rate
    if game_state["rounds_played"] > 0:
        win_rate = (game_state["wins"] / game_state["rounds_played"]) * 100
        print(f"อัตราการชนะ: {win_rate:.2f}%")

    print("=" * 50)


def check_game_over(game_state):
    """Check if player has run out of money."""
    if game_state["balance"] < min(VALID_BETS):
        print("\n💔 กลับบ้านเถอะไม่เหลือเหี้ยไรแล้ว")
        return True
    return False


def display_game_over(game_state):
    """Display game over message and final statistics."""
    print("\n" + "=" * 50 + "\n🎮 จบเกม\n")

    profit = game_state["balance"] - INITIAL_BALANCE
    if profit > 0:
        print(f"🎉 คุณได้กำไร: {profit:.2f} บาท")
    elif profit < 0:
        print(f"😢 คุณขาดทุน: {abs(profit):.2f} บาท")
    else:
        print("⚖️ คุณเสมอตัว!")


def main() -> None:
    """Main game loop."""

    game_state = start_game()

    while True:
        if check_game_over(game_state):
            display_game_over(game_state)
            break

        bet = get_bet(game_state["balance"])

        if bet == VIEW_STATS_CODE:
            display_statistics(game_state)
            continue
        elif bet == EXIT_CODE:
            display_game_over(game_state)
            break

        guess = get_guess()
        game_state = play_round(game_state, bet, guess)


if __name__ == "__main__":
    main()
