from src.ai.gemini import generate_response


def start_chat_loop():
    while True:
        msg = input("> ").strip()

        if not msg:
            print(
                "invalid input.\nmust contain at least one letter and cannot be whitespace!",
            )
            continue

        if msg == "exit":
            break

        reply = generate_response(msg)

        print(reply)
