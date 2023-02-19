import requests
import random
import string
import time 
import re

class Debate:
    def __init__(self, first_debater_api, second_debater_api, topic):
        self.topic = topic
        self.first_debater_api = first_debater_api
        self.second_debater_api = second_debater_api
        self.first_debater = None
        self.second_debater = None
        self.scores = {"first_debater": 0, "second_debater": 0}
        self.winner = None
        self.debate_ready = False

        self.debate_setup()

    def run_debate(self):
        if self.debate_ready:
            print("The debate is ready to begin")
            rounds = ["introductions", "opening_statement", "cross_examination", "rebuttal", "final_focus", "conclusion", "end"]
            for a_round in rounds:
                time.sleep(1)
                eval("self." + a_round + "()")


        else:
            print("One or more participants are not ready to debate. Please check that APIs are live and ready.")

    def debate_setup(self):
        first_debater_setup = f'{self.first_debater_api}/debater'
        second_debater_setup = f'{self.second_debater_api}/debater'
        response_1 = requests.get(first_debater_setup)
        response_2 = requests.get(second_debater_setup)
        if response_1.status_code == 200 and response_2.status_code == 200:
            self.first_debater = response_1.json()
            self.second_debater = response_2.json()
            self.debate_ready = True


    def introductions(self):
        print("-----------------------------INTRODUCTIONS-----------------------------")
        print()
        print(f"Welcome to our debate!")
        time.sleep(0.1)
        print(f"Today we will be hearing all about the topic: {self.topic}")
        time.sleep(0.1)
        print(f"The first debater is {self.first_debater.get('name')}")
        time.sleep(0.1)
        print(f"The second debater is {self.second_debater.get('name')}")
        time.sleep(0.1)
        print()
        time.sleep(0.1)
        print(f"Please introduce yourself {self.first_debater.get('name')}")
        time.sleep(0.1)
        print()
        time.sleep(0.1)
        print(f"Hi I am {self.first_debater.get('name')}. {self.first_debater.get('introduction')}")
        time.sleep(0.1)
        print()
        time.sleep(0.1)
        print(f"Please introduce yourself {self.second_debater.get('name')}")
        time.sleep(0.1)
        print()
        print(f"{self.second_debater.get('introduction')}. Oh, right and my name is {self.second_debater.get('name')}")
        print()
        print()

    def opening_statement(self):
        print("-----------------------------OPENTING STATEMENTS-----------------------------")
        params = {"topic": self.topic}
        d1_opening_statement_url = f'{self.first_debater_api}/opening_statement'
        d1_response = requests.get(d1_opening_statement_url, params=params)
        d1_data = d1_response.json()
        d1_opening_statement = d1_data.get('response')
        
        d2_opening_statement_url = f'{self.second_debater_api}/opening_statement'
        d2_response = requests.get(d2_opening_statement_url, params=params)
        d2_data = d2_response.json()
        d2_opening_statement = d2_data.get('response')

        #print("Ladies and Gentlemen it is now time for each side to give their opening statements. In this first part, each side will present their initial arguments and set the stage for the rest of the discussion. The goal is to introduce our perspectives and convince you, the audience, of our position on the topic at hand.")
        print()
        print()
        print("Alright, listen up y'all. It's time to lay down the facts and make our case in the opening statements. You best believe we're gonna come out swingin' with some truth bombs and hard evidence.")

        round_results = self.round_scoring(d1_opening_statement, d2_opening_statement)
        

    def cross_examination(self):
        print("-----------------------------CROSS EXAMINATIONSS-----------------------------")
        params = {"topic": self.topic}
        d1_opening_statement_url = f'{self.first_debater_api}/opening_statement'
        d1_response = requests.get(d1_opening_statement_url, params=params)
        d1_data = d1_response.json()
        d1_opening_statement = d1_data.get('response')
        
        d2_opening_statement_url = f'{self.second_debater_api}/opening_statement'
        d2_response = requests.get(d2_opening_statement_url, params=params)
        d2_data = d2_response.json()
        d2_opening_statement = d2_data.get('response')

        print()
        print()
        #print("Thank you for the opening statements. Now, it's time for the cross-examination, where each side will have the opportunity to question the other about their arguments. The goal is to probe deeper into each other's claims and evidence, and to identify any weaknesses or gaps in the opposing argument.")
        print("Now we're gonna get down and dirty, baby. It's time to grill these fools and expose their weak points during the cross examination. Ain't no dodging the tough questions today.")

        round_results = self.round_scoring(d1_opening_statement, d2_opening_statement)
        

    def rebuttal(self):
        print("-----------------------------REBUTTAL-----------------------------")
        params = {"topic": self.topic}
        d1_opening_statement_url = f'{self.first_debater_api}/opening_statement'
        d1_response = requests.get(d1_opening_statement_url, params=params)
        d1_data = d1_response.json()
        d1_opening_statement = d1_data.get('response')
        
        d2_opening_statement_url = f'{self.second_debater_api}/opening_statement'
        d2_response = requests.get(d2_opening_statement_url, params=params)
        d2_data = d2_response.json()
        d2_opening_statement = d2_data.get('response')

        print()
        print()
        #print("Thank you for the insightful cross-examination. In this part of the debate, each side will try to rebut the arguments of the other. The goal is to counter the opposing arguments with stronger evidence or to show that the opposing arguments are flawed in some way.")
        print("Oh, so you wanna come at us with your weak sauce arguments? Ha! We ain't scared of your nonsense. We're gonna tear your case apart and leave you shakin' in your boots during the rebuttal part of this debate.")

        round_results = self.round_scoring(d1_opening_statement, d2_opening_statement)

    def final_focus(self):
        print("-----------------------------FINAL FOCUS-----------------------------")
        params = {"topic": self.topic}
        d1_opening_statement_url = f'{self.first_debater_api}/opening_statement'
        d1_response = requests.get(d1_opening_statement_url, params=params)
        d1_data = d1_response.json()
        d1_opening_statement = d1_data.get('response')
        
        d2_opening_statement_url = f'{self.second_debater_api}/opening_statement'
        d2_response = requests.get(d2_opening_statement_url, params=params)
        d2_data = d2_response.json()
        d2_opening_statement = d2_data.get('response')

        #print("We're approaching the end of our debate, and it's time for the final focus. Each side will have one last chance to make a strong case for their position. The goal is to leave the audience with a lasting impression of our arguments and to make a final appeal to their reasoning and emotions.")
        print()
        print()
        print("This is it, folks. The moment of truth. It's the final focus. We've laid out our case, rebutted their arguments, and now it's time to bring it home. We're gonna hit 'em with our best shot and leave 'em speechless.")

        round_results = self.round_scoring(d1_opening_statement, d2_opening_statement)

    def conclusion(self):
        print("-----------------------------CONCLUSIONS-----------------------------")
        params = {"topic": self.topic}
        d1_opening_statement_url = f'{self.first_debater_api}/opening_statement'
        d1_response = requests.get(d1_opening_statement_url, params=params)
        d1_data = d1_response.json()
        d1_opening_statement = d1_data.get('response')
        
        d2_opening_statement_url = f'{self.second_debater_api}/opening_statement'
        d2_response = requests.get(d2_opening_statement_url, params=params)
        d2_data = d2_response.json()
        d2_opening_statement = d2_data.get('response')

        #print("Thank you to both sides for a stimulating debate. In this final part, we will summarize our arguments and conclude our discussion. The goal is to provide closure to the debate and to help the audience come to a decision on the topic at hand.")
        print()
        print()
        print("And there you have it, ladies and gents. The gloves are off, the dust has settled, and we're about to see who came out on top in the conclusion. Ain't no doubt in my mind who the real winner is here today.")

        round_results = self.round_scoring(d1_opening_statement, d2_opening_statement)


    def end(self):
        if self.scores.get('first_debater')  > self.scores.get('second_debater'):
            self.winner = self.first_debater.get('name')
        elif self.scores.get('first_debater') < self.scores.get('second_debater'):
            self.winner = self.second_debater.get('name')
        else:
            self.winner = "...it's a tie!"
        print()
        print()
        print(f"Thank you for joining our debate on {self.topic}!")
        print(f"The final results were {self.first_debater.get('name')} with {self.scores.get('first_debater')} rounds won and {self.second_debater.get('name')} with {self.scores.get('second_debater')} rounds won!")
        print(f"The winner is {self.winner}!")

    def round_scoring(self, debater_1_text, debater_2_text):
        coin_toss = random.choice([-1,1])
        mystery_letter = random.choice(string.ascii_lowercase)
        def score_method_unique_words(text):
            all_words = text.split()
            return len(set(all_words))
        
        def score_method_repeat_word(text):
            text = text.lower()
            all_words = text.split()
            word_counts = {}

            for word in all_words:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

            most_common_word = max(word_counts, key=word_counts.get)
            return word_counts[most_common_word]

        def score_method_vowels(text):
            text = text.lower()
            vowels = "aeiou"
            vowel_count = 0
            for char in text:
                if char in vowels:
                    vowel_count += 1
            return vowel_count

        def score_method_alliterations(text):
            text = text.lower()
            pattern = re.compile(r'\b(\w)\w*\s+\b\1\w*', re.IGNORECASE)
            matches = pattern.findall(text)
            return len(matches)
            
        def score_method_mystery_letter(text):
            text = text.lower()
            regex = re.compile(r'{}'.format(mystery_letter), re.IGNORECASE)
            matches = regex.findall(text)
            return len(matches)

        def score_method_mention_topic(text):
            text = text.lower()
            word = self.topic
            if word == 'dandd':
                word = 'd&d'
            regex = re.compile(r'\b{}\b'.format(word), re.IGNORECASE)
            matches = regex.findall(text)
            return len(matches)
        

        scoring_functions = ["score_method_unique_words", "score_method_repeat_word", "score_method_vowels", "score_method_alliterations", "score_method_mystery_letter", "score_method_mention_topic"]
        score_method_string = random.choice(scoring_functions)
        score_method = eval(score_method_string)
        round_results = {}
        round_results["score_method"] = score_method_string
        round_results["debater_1_score"] = score_method(debater_1_text)
        round_results["debater_2_score"] = score_method(debater_2_text)
        if coin_toss == 1:
            round_results["more_or_less"] = "more"
        elif coin_toss == -1:
            round_results["more_or_less"] = "less"
        
        if coin_toss*round_results["debater_1_score"] > coin_toss*round_results["debater_2_score"]:
            round_results["winner"] = self.first_debater.get('name')
            self.scores['first_debater'] += 1
        elif coin_toss*round_results["debater_1_score"] < coin_toss*round_results["debater_2_score"]:
            round_results["winner"] = self.second_debater.get('name')
            self.scores['second_debater'] += 1
        else:
            round_results["winner"] = "a tie"
        
        print()
        print("For this round we are going to use the following scoring method:")
        print()
        if score_method_string == "score_method_unique_words": 
            print(f"Whoever uses {round_results.get('more_or_less')} unique words in their answer will win the round!")
        elif score_method_string == "score_method_repeat_word":
            print(f"Whoever uses their most used word {round_results.get('more_or_less')} than their opponent will win the round!")
        elif score_method_string == "score_method_vowels":
            print(f"Whoever uses {round_results.get('more_or_less')} vowels in their answer will win the round!")
        elif score_method_string == "score_method_alliterations":
            print(f"Whoever uses {round_results.get('more_or_less')} alliterations (consequtive words with the same letter) in their answer will win the round!")
        elif score_method_string == "score_method_mystery_letter":
            print(f"Whoever uses the letter '{mystery_letter}' {round_results.get('more_or_less')} in their answer will win the round!")
        elif score_method_string == "score_method_mention_topic":
            print(f"Whoever uses the name of the topic {round_results.get('more_or_less')} in their answer will win the round!")

        print()
        print()
        time.sleep(0.5)
        print(f"{self.first_debater.get('name')}: {debater_1_text}")
        print()
        time.sleep(0.5)
        print(f"{self.second_debater.get('name')}: {debater_2_text}")
        print()
        time.sleep(0.5)
        print(f"{self.first_debater.get('name')} got a score of {round_results.get('debater_1_score')} and {self.second_debater.get('name')} got a score of {round_results.get('debater_2_score')}!")
        time.sleep(0.2)
        print(f"The winner of this round is {round_results.get('winner')}!") 
        print()
        print()

        return(round_results)
            
            
            





