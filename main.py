import  random
class game:
    def __init__(self):
        self.secreat_code = []
        for i in range(4):
            self.secreat_code.append(str(random.randint(0,9)))
    def check(self, guess):
        result = []
        guess_list = []
        for i in guess:
            guess_list.append(i)
        counter = 0
        signed_munbers = []
        for i in range(4):
            while signed_munbers.count(guess_list[i]) == 0:
                if self.secreat_code[i] == guess_list [i]:
                    result.append("B")
                    counter += 1
                else:
                    for j in range(4):
                        if self.secreat_code[i] == guess_list [j]:
                            if self.secreat_code.count(guess_list[j]) >= guess_list.count(guess_list[j]):
                                result.append("C")
                                break
                            else:
                                result.append("C")
                                signed_munbers.append(guess_list[i])
                                break
        result = result.sort()
        return result
