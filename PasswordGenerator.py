import random
import string

randomnumber_list = [random.randint(1,5) for i in range(4)]
lowercase_chrs = random.sample(string.ascii_lowercase,randomnumber_list[0])
uppercase_chrs = random.sample(string.ascii_uppercase,randomnumber_list[1])
some_digits = random.sample(string.digits,randomnumber_list[2])
some_other_chr = random.sample(["!","@","#","$","%","*"],randomnumber_list[3])

total_pass_list = lowercase_chrs + uppercase_chrs + some_digits + some_other_chr
random.shuffle(total_pass_list)
empty_str = ""
total_pass = empty_str.join(total_pass_list)
print(f"Generated Password Is: {total_pass}")
