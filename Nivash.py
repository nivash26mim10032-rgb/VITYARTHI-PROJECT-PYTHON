import random

# Base question pool (You can scale this list up to 200 questions by following the same dictionary format)
QUESTION_POOL = [
    # --- Base Questions ---
    {"q": "What is the capital of France?", "options": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"], "answer": "C"},
    {"q": "Which programming language is known as the snake?", "options": ["A. Java", "B. Python", "C. C++", "D. Ruby"], "answer": "B"},
    {"q": "What is 5 + 3 * 2?", "options": ["A. 16", "B. 11", "C. 13", "D. 10"], "answer": "B"},
    {"q": "Which planet is known as the Red Planet?", "options": ["A. Venus", "B. Saturn", "C. Mars", "D. Jupiter"], "answer": "C"},
    {"q": "Who wrote 'Hamlet'?", "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. Leo Tolstoy"], "answer": "B"},
    {"q": "What is the boiling point of water in Celsius?", "options": ["A. 90", "B. 100", "C. 120", "D. 80"], "answer": "B"},
    {"q": "Which gas do plants absorb from the atmosphere?", "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"], "answer": "C"},
    {"q": "What is the largest mammal on Earth?", "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Great White Shark"], "answer": "B"},
    {"q": "In which year did World War II end?", "options": ["A. 1940", "B. 1945", "C. 1950", "D. 1939"], "answer": "B"},
    {"q": "What is the square root of 144?", "options": ["A. 10", "B. 11", "C. 12", "D. 14"], "answer": "C"},
    {"q": "Which element has the chemical symbol 'O'?", "options": ["A. Gold", "B. Oxygen", "C. Silver", "D. Iron"], "answer": "B"},
    {"q": "How many continents are there on Earth?", "options": ["A. 5", "B. 6", "C. 7", "D. 8"], "answer": "C"},
    
    # --- Additional 88 Questions ---
    {"q": "Which country is home to the kangaroo?", "options": ["A. New Zealand", "B. Australia", "C. South Africa", "D. Brazil"], "answer": "B"},
    {"q": "What is the hardest natural substance on Earth?", "options": ["A. Gold", "B. Iron", "C. Diamond", "D. Platinum"], "answer": "C"},
    {"q": "Who painted the Mona Lisa?", "options": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet"], "answer": "C"},
    {"q": "What is the smallest planet in our solar system?", "options": ["A. Mars", "B. Mercury", "C. Venus", "D. Pluto"], "answer": "B"},
    {"q": "Which ocean is the largest on Earth?", "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"], "answer": "D"},
    {"q": "What is the chemical symbol for gold?", "options": ["A. Ag", "B. Au", "C. Gd", "D. Go"], "answer": "B"},
    {"q": "In what year did the Titanic sink?", "options": ["A. 1912", "B. 1905", "C. 1920", "D. 1898"], "answer": "A"},
    {"q": "What is the main ingredient in guacamole?", "options": ["A. Tomato", "B. Avocado", "C. Lime", "D. Onion"], "answer": "B"},
    {"q": "How many players are on the field for a soccer team?", "options": ["A. 9", "B. 10", "C. 11", "D. 12"], "answer": "C"},
    {"q": "What language is spoken in Brazil?", "options": ["A. Spanish", "B. Portuguese", "C. French", "D. Italian"], "answer": "B"},
    {"q": "What is the tallest mountain in the world?", "options": ["A. K2", "B. Kangchenjunga", "C. Mount Everest", "D. Kilimanjaro"], "answer": "C"},
    {"q": "Which instrument has 88 keys?", "options": ["A. Guitar", "B. Violin", "C. Piano", "D. Flute"], "answer": "C"},
    {"q": "What is the capital of Japan?", "options": ["A. Seoul", "B. Beijing", "C. Tokyo", "D. Kyoto"], "answer": "C"},
    {"q": "Who discovered penicillin?", "options": ["A. Alexander Fleming", "B. Marie Curie", "C. Albert Einstein", "D. Isaac Newton"], "answer": "A"},
    {"q": "What is the speed of light approximately?", "options": ["A. 300,000 km/s", "B. 150,000 km/s", "C. 1,000 km/s", "D. 3,000,000 km/s"], "answer": "A"},
    {"q": "Which country hosted the 2016 Summer Olympics?", "options": ["A. China", "B. Brazil", "C. United Kingdom", "D. Greece"], "answer": "B"},
    {"q": "What is the currency of the United Kingdom?", "options": ["A. Euro", "B. Dollar", "C. Pound Sterling", "D. Franc"], "answer": "C"},
    {"q": "Which animal is known as the 'Ship of the Desert'?", "options": ["A. Horse", "B. Elephant", "C. Camel", "D. Donkey"], "answer": "C"},
    {"q": "What is the freezing point of water in Fahrenheit?", "options": ["A. 0°F", "B. 32°F", "C. 100°F", "D. 212°F"], "answer": "B"},
    {"q": "Who wrote the 'Harry Potter' series?", "options": ["A. J.R.R. Tolkien", "B. J.K. Rowling", "C. George R.R. Martin", "D. Stephen King"], "answer": "B"},
    {"q": "What is the largest desert in the world?", "options": ["A. Sahara Desert", "B. Arabian Desert", "C. Gobi Desert", "D. Antarctic Desert"], "answer": "D"},
    {"q": "Which organ in the human body produces insulin?", "options": ["A. Liver", "B. Pancreas", "C. Kidney", "D. Heart"], "answer": "B"},
    {"q": "What does CPU stand for in computer science?", "options": ["A. Central Processing Unit", "B. Computer Personal Unit", "C. Central Program Utility", "D. Core Processing Utility"], "answer": "A"},
    {"q": "Which U.S. state is known as the Sunshine State?", "options": ["A. California", "B. Texas", "C. Florida", "D. Hawaii"], "answer": "C"},
    {"q": "What is the chemical symbol for table salt?", "options": ["A. H2O", "B. NaCl", "C. CO2", "D. KCl"], "answer": "B"},
    {"q": "How many bones are in the adult human body?", "options": ["A. 206", "B. 210", "C. 198", "D. 215"], "answer": "A"},
    {"q": "Which gas makes up the majority of Earth's atmosphere?", "options": ["A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Hydrogen"], "answer": "C"},
    {"q": "What is the national flower of Japan?", "options": ["A. Rose", "B. Cherry Blossom", "C. Lotus", "D. Tulip"], "answer": "B"},
    {"q": "Who was the first person to walk on the Moon?", "options": ["A. Buzz Aldrin", "B. Yuri Gagarin", "C. Neil Armstrong", "D. Michael Collins"], "answer": "C"},
    {"q": "What is the hardest rock?", "options": ["A. Granite", "B. Marble", "C. Diamond", "D. Quartz"], "answer": "C"},
    {"q": "Which country is the largest by land area?", "options": ["A. Canada", "B. China", "C. United States", "D. Russia"], "answer": "D"},
    {"q": "What is the primary color of a school bus in the US?", "options": ["A. Red", "B. Yellow", "C. Orange", "D. Blue"], "answer": "B"},
    {"q": "Which planet is closest to the Sun?", "options": ["A. Venus", "B. Mercury", "C. Earth", "D. Mars"], "answer": "B"},
    {"q": "What is the value of Pi (to two decimal places)?", "options": ["A. 3.12", "B. 3.14", "C. 3.16", "D. 3.18"], "answer": "B"},
    {"q": "Who invented the telephone?", "options": ["A. Thomas Edison", "B. Nikola Tesla", "C. Alexander Graham Bell", "D. Guglielmo Marconi"], "answer": "C"},
    {"q": "What is the capital of Canada?", "options": ["A. Toronto", "B. Vancouver", "C. Ottawa", "D. Montreal"], "answer": "C"},
    {"q": "Which sport uses terms like 'strike', 'spare', and 'turkey'?", "options": ["A. Golf", "B. Bowling", "C. Tennis", "D. Baseball"], "answer": "B"},
    {"q": "What is the longest river in the world?", "options": ["A. Amazon River", "B. Nile River", "C. Yangtze River", "D. Mississippi River"], "answer": "B"},
    {"q": "Which vitamin is produced when a person is exposed to sunlight?", "options": ["A. Vitamin A", "B. Vitamin B", "C. Vitamin C", "D. Vitamin D"], "answer": "D"},
    {"q": "What is the capital of Australia?", "options": ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Brisbane"], "answer": "C"},
    {"q": "Which superhero is also known as Bruce Wayne?", "options": ["A. Superman", "B. Iron Man", "C. Batman", "D. Spider-Man"], "answer": "C"},
    {"q": "What is the study of weather called?", "options": ["A. Geology", "B. Meteorology", "C. Astronomy", "D. Ecology"], "answer": "B"},
    {"q": "Which element has the atomic number 1?", "options": ["A. Helium", "B. Hydrogen", "C. Oxygen", "D. Carbon"], "answer": "B"},
    {"q": "What is the main language spoken in Argentina?", "options": ["A. Portuguese", "B. Spanish", "C. English", "D. German"], "answer": "B"},
    {"q": "Who painted 'The Starry Night'?", "options": ["A. Claude Monet", "B. Vincent van Gogh", "C. Pablo Picasso", "D. Salvador Dali"], "answer": "B"},
    {"q": "What is the hardest substance in the human body?", "options": ["A. Bone", "B. Tooth Enamel", "C. Cartilage", "D. Nail"], "answer": "B"},
    {"q": "Which metal is liquid at room temperature?", "options": ["A. Iron", "B. Mercury", "C. Lead", "D. Zinc"], "answer": "B"},
    {"q": "What is the capital of Italy?", "options": ["A. Venice", "B. Milan", "C. Rome", "D. Florence"], "answer": "C"},
    {"q": "Which continent is the Sahara Desert located on?", "options": ["A. Asia", "B. Africa", "C. Australia", "D. South America"], "answer": "B"},
    {"q": "What does HTTP stand for in web addresses?", "options": ["A. HyperText Transfer Protocol", "B. HyperText Transmission Program", "C. High Transfer Text Protocol", "D. Hyperlink Transfer Technology"], "answer": "A"},
    {"q": "How many sides does a hexagon have?", "options": ["A. 5", "B. 6", "C. 7", "D. 8"], "answer": "B"},
    {"q": "Which bird is universally known as a symbol of peace?", "options": ["A. Eagle", "B. Dove", "C. Owl", "D. Swan"], "answer": "B"},
    {"q": "What is the capital of Egypt?", "options": ["A. Alexandria", "B. Cairo", "C. Luxor", "D. Giza"], "answer": "B"},
    {"q": "Which planet has the most moons?", "options": ["A. Saturn", "B. Jupiter", "C. Uranus", "D. Neptune"], "answer": "B"},
    {"q": "Who wrote 'The Odyssey'?", "options": ["A. Homer", "B. Socrates", "C. Plato", "D. Aristotle"], "answer": "A"},
    {"q": "What is the smallest country in the world?", "options": ["A. Monaco", "B. Liechtenstein", "C. Vatican City", "D. San Marino"], "answer": "C"},
    {"q": "Which animal is the fastest land animal?", "options": ["A. Lion", "B. Cheetah", "C. Pronghorn", "D. Leopard"], "answer": "B"},
    {"q": "What is the currency of Japan?", "options": ["A. Yuan", "B. Yen", "C. Won", "D. Ringgit"], "answer": "B"},
    {"q": "Which blood type is known as the universal donor?", "options": ["A. A", "B. B", "C. AB", "D. O negative"], "answer": "D"},
    {"q": "What is the chemical formula for water?", "options": ["A. CO2", "B. H2O", "C. O2", "D. NaCl"], "answer": "B"},
    {"q": "Who sculpted the statue of David?", "options": ["A. Donatello", "B. Michelangelo", "C. Raphael", "D. Leonardo da Vinci"], "answer": "B"},
    {"q": "What is the largest internal organ in the human body?", "options": ["A. Heart", "B. Liver", "C. Lungs", "D. Kidney"], "answer": "B"},
    {"q": "Which gas is used in bright neon store signs?", "options": ["A. Helium", "B. Neon", "C. Argon", "D. Krypton"], "answer": "B"},
    {"q": "What is the capital of Spain?", "options": ["A. Barcelona", "B. Valencia", "C. Madrid", "D. Seville"], "answer": "C"},
    {"q": "How many players are on the ice for one hockey team during play?", "options": ["A. 5", "B. 6", "C. 7", "D. 8"], "answer": "B"},
    {"q": "Which company created the iPhone?", "options": ["A. Microsoft", "B. Google", "C. Apple", "D. Samsung"], "answer": "C"},
    {"q": "What is the main component of the sun?", "options": ["A. Liquid lava", "B. Hydrogen and Helium", "C. Oxygen and Nitrogen", "D. Carbon and Iron"], "answer": "B"},
    {"q": "Which European country is shaped like a boot?", "options": ["A. Spain", "B. Greece", "C. Italy", "D. France"], "answer": "C"},
    {"q": "What is the speed of sound in air approximately?", "options": ["A. 343 meters per second", "B. 100 meters per second", "C. 1,000 meters per second", "D. 50 meters per second"], "answer": "A"},
    {"q": "Who is the author of 'The Lord of the Rings'?", "options": ["A. C.S. Lewis", "B. J.R.R. Tolkien", "C. Roald Dahl", "D. Charles Dickens"], "answer": "B"},
    {"q": "What is the tallest animal in the world?", "options": ["A. Elephant", "B. Giraffe", "C. Moose", "D. Camel"], "answer": "B"},
    {"q": "Which planet is known as the Blue Planet?", "options": ["A. Neptune", "B. Uranus", "C. Earth", "D. Venus"], "answer": "C"},
    {"q": "What is the capital of Germany?", "options": ["A. Munich", "B. Frankfurt", "C. Berlin", "D. Hamburg"], "answer": "C"},
    {"q": "Which instrument family does the saxophone belong to?", "options": ["A. Strings", "B. Percussion", "C. Woodwind", "D. Brass"], "answer": "C"},
    {"q": "What is the main function of red blood cells?", "options": ["A. Fight infections", "B. Carry oxygen", "C. Clot blood", "D. Digest food"], "answer": "B"},
    {"q": "Who discovered gravity when an apple fell on his head?", "options": ["A. Albert Einstein", "B. Isaac Newton", "C. Galileo Galilei", "D. Nikola Tesla"], "answer": "B"},
    {"q": "What is the capital of India?", "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Bengaluru"], "answer": "B"},
    {"q": "Which element's symbol is 'Fe'?", "options": ["A. Iron", "B. Fluorine", "C. Francium", "D. Fermium"], "answer": "A"},
    {"q": "What is the largest island in the world?", "options": ["A. Madagascar", "B. Greenland", "C. New Guinea", "D. Borneo"], "answer": "B"},
    {"q": "Which sport is played at Wimbledon?", "options": ["A. Cricket", "B. Golf", "C. Tennis", "D. Polo"], "answer": "C"},
    {"q": "What is the capital of South Korea?", "options": ["A. Busan", "B. Seoul", "C. Incheon", "D. Daegu"], "answer": "B"},
    {"q": "Which gas do humans exhale most when breathing out?", "options": ["A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Hydrogen"], "answer": "B"},
    {"q": "What is the chemical symbol for silver?", "options": ["A. Si", "B. Ag", "C. Sr", "D. Al"], "answer": "B"},
    {"q": "Who wrote 'Pride and Prejudice'?", "options": ["A. Charlotte Bronte", "B. Jane Austen", "C. Emily Bronte", "D. Virginia Woolf"], "answer": "B"},
    {"q": "What is the hottest planet in our solar system?", "options": ["A. Mercury", "B. Venus", "C. Mars", "D. Jupiter"], "answer": "B"},
    {"q": "Which country has the most natural lakes?", "options": ["A. United States", "B. Russia", "C. Canada", "D. Australia"], "answer": "C"},
    {"q": "What is the currency of the United States?", "options": ["A. Peso", "B. Dollar", "C. Euro", "D. Pound"], "answer": "B"},
    {"q": "Which ocean is the smallest by surface area?", "options": ["A. Indian Ocean", "B. Atlantic Ocean", "C. Arctic Ocean", "D. Southern Ocean"], "answer": "C"}
]

def run_quiz():
    print("========================================")
    print("         WELCOME TO THE QUIZ BOWL       ")
    print("========================================")
    
    # Randomly select 10 questions (or max available if pool is smaller)
    num_questions_to_ask = min(10, len(QUESTION_POOL))
    selected_questions = random.sample(QUESTION_POOL, num_questions_to_ask)
    
    score = 0
    
    for idx, item in enumerate(selected_questions, 1):
        print(f"\nQuestion {idx}: {item['q']}")
        for option in item['options']:
            print(option)
            
        try:
            user_answer = input("Your answer (A/B/C/D): ").strip().upper()
            
            # Basic validation
            if user_answer not in ['A', 'B', 'C', 'D']:
                print("⚠️ Invalid choice format. Marked as incorrect.")
                continue
                
            if user_answer == item['answer']:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Incorrect. The correct answer was {item['answer']}.")
                
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Moving to next question.")
            
    print("\n========================================")
    print("              QUIZ FINISHED             ")
    print("========================================")
    print(f"Your Final Score: {score} / {num_questions_to_ask}")
    percentage = (score / num_questions_to_ask) * 100
    print(f"Percentage: {percentage:.2f}%")

if __name__ == "__main__":
    run_quiz()