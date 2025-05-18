import requests

BASE_URL = "https://wordle.votee.dev:8000"

def check_guessing(guess_word, size, seed):
    endpoint = f"{BASE_URL}/random"
    payload = {
        "guess": guess_word,
        "size": size,
        "seed": seed
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.get(endpoint, params=payload, headers=headers)

    result = []

    if response.status_code == 200:
        data = response.json()
        for _ in data:
            result.append(_['result'])

        return result
    else:
        print(f"Error: {response.status_code}")
        return None
    
def reconstruct_guess(word_length, check_list, attempts, old_guess):
    letters_by_frequency = [
        "e","t","a","o","i","n","s","h","r","d",
        "l","u","c","m","f","g","w","y","p","b",
        "v","k","j","x","q","z"]
    new_guess = [''] * word_length
    for i in range(word_length):
        if check_list[i] == 1:
            new_guess[i] = old_guess[i]
        else:
            new_guess[i] = letters_by_frequency[attempts]
    
    return ''.join(new_guess)

if __name__ == "__main__":
    word_length = 7 # word length can be any integer
    seed = 123456789 # Replace with your desired seed

    # Initialize the parameters
    guess = 'e' * word_length
    check_list = [0] * word_length
    attempts = 0

    while attempts < 26:
        if attempts > 0:
            guess = reconstruct_guess(word_length, check_list, attempts, guess)
        guess_result = check_guessing(guess, word_length, seed)

        for i in range(word_length):
            if guess_result[i] == 'correct':
                check_list[i] = 1
            elif guess_result[i] == 'present':
                continue
            elif guess_result[i] == 'absent':
                break

        print(f"Attempt {attempts}: {guess} - Result: {guess_result}")
        if 'present' not in guess_result and 'absent' not in guess_result:
            print(f"Found the word: {guess}")
            break
        attempts += 1