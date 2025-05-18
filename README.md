# Word-guessing Program

This repository contains three Python scripts that attempt to guess a given word using a **frequency-based** strategy, somewhat reminiscent of a Wordle-style guessing process. The three scripts interact with a remote service using three APIs to determine whether each guessed letter is **correct**, **present**, or **absent**. Based on the feedback of the current guessing, the program modify its guessing based on the English character frequency. As a result, the worst case of the guessing is 26 iterations and the final result is guarnteed to converge.

---

## Logic of checking the guessing result

### 1. `guessing_daily.py`
The script checks the guessing through "https://wordle.votee.dev:8000/daily" to guess against the daily puzzle. The input requires the size of the guessing word.

### 2. `guessing_random.py`
The script checks the guessing through "https://wordle.votee.dev:8000/random" to guess against a random word. The input requires the size of the guessing word and a seed.

### 3. `guessing_word.py`
The script checks the guessing through "https://wordle.votee.dev:8000/word/{word}" to guess against a selected word. The input only requires the selected word.

---

## Logic of reconstructing the next guess
As we get the result of our previous guess, we need to modify our guess based on this result. The three scripts utilize the same algorithm in this reconstruction guessing stage.
The guessing is in the sequency of the frequency of the English characters in the real life. The list of letters by descending frequency is shown below:
letters_by_frequency = [
        "e","t","a","o","i","n","s","h","r","d",
        "l","u","c","m","f","g","w","y","p","b",
        "v","k","j","x","q","z"]
Therefore, we can guess the characters in the order in this list. When we guess a char correctly, we mark the position in the word to lock that position so that in future guessing, no modification will be applied to that loecked position. When we guess a char wrongly, we do not do action.
For example, when the guessing answer is 'apple', and the guess is 'abcde', we mark the right-guessing positions in the check_list to 1. [0, 0, 0, 0, 0] to [1, 0, 0, 0, 1].
Since 'e' is the most frequency used char, we always initialize our first guess as 'eee...e'

---

## Requirements

- **Python 3.x**  
- **Requests library** (install with `pip install requests`)

---

## Usage

1. **Clone or download** this repository.  
2. **Install dependencies**:  
   ```bash
   pip install requests

## Author Information
**Name** Zhao Wenzhe

**Email** wenzhe.zhao@outlook.com
