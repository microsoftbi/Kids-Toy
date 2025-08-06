import random
import pyttsx3

def init_voice_engine():
    """初始化语音引擎"""
    engine = pyttsx3.init()
    # 可以调整语速，范围一般在50-200之间
    engine.setProperty('rate', 150)
    return engine

def get_valid_integer(prompt, min_value=None):
    """获取用户输入的有效整数，确保输入符合要求"""
    while True:
        try:
            num = int(input(prompt))
            if min_value is not None and num < min_value:
                print(f"请输入大于等于{min_value}的数字！")
                continue
            return num
        except ValueError:
            print("输入无效，请输入一个整数！")

def generate_question(max_num):
    """生成一道加减法题目，确保：
    1. 两个数字都不为0
    2. 计算结果不为0
    3. 减法结果非负
    """
    while True:
        # 生成两个1到max_num之间的随机数（确保不为0）
        num1 = random.randint(1, max_num)
        num2 = random.randint(1, max_num)
        
        # 随机选择加法或减法
        if random.choice([True, False]):
            # 加法
            answer = num1 + num2
            question = f"{num1} + {num2} = ?"
        else:
            # 减法，确保结果非负且不为0
            if num1 <= num2:
                continue  # 如果被减数小于等于减数，跳过当前组合重新生成
            answer = num1 - num2
            question = f"{num1} - {num2} = ?"
        
        # 确保结果不为0才返回
        if answer != 0:
            return question, answer

def main():
    # 初始化语音引擎
    engine = init_voice_engine()
    print("欢迎来到算术练习应用！")
    
    # 获取用户设定的数字范围（至少为1，因为我们不允许0出现）
    max_num = get_valid_integer("请输入数字范围（例如输入10表示10以内的加减法）：", 1)
    
    # 获取用户设定的题目数量
    num_questions = get_valid_integer("请输入要生成的题目数量：", 1)
    
    print(f"\n好的，现在开始{max_num}以内的算术练习，共{num_questions}道题。")
    print("所有题目中不会出现数字0，计算结果也不会是0。")
    print("请认真作答，答错将需要重新回答直到正确为止。\n")
    
    # 开始答题
    for i in range(num_questions):
        question, correct_answer = generate_question(max_num)
        
        while True:
            try:
                user_answer = int(input(f"第{i+1}题：{question} "))
                
                if user_answer == correct_answer:
                    print("回答正确！\n")
                    break
                else:
                    print("回答错误，请重新计算！")
                    # 语音提示错误
                    engine.say("回答错误，请重新计算。")
                    engine.runAndWait()
            except ValueError:
                print("输入无效，请输入一个整数作为答案！")
                engine.say("输入无效，请输入一个整数作为答案。")
                engine.runAndWait()
    
    print("恭喜你完成了所有题目！")
    engine.say("恭喜你完成了所有题目！")
    engine.runAndWait()
    
    # 关闭语音引擎
    engine.stop()

if __name__ == "__main__":
    main()
    
