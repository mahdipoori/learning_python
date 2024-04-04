import re
def main():
    _0text = "sokanacademykjhgfds" #TODO all of specific cracter is after cracters
    text="cat"                  #TODO'rat'
    _0regex = r"sokanacademy."  #TODO if use \ you use escapting for caracter like "." etc
    regex= r"[cm]at"            #TODO [] is Character Set// [^cm] Caret "^" every alphbet except c and m
                                #TODO "[A-Za-z0-9]" == "\w" != \W
                                #TODO "[0-9]" == "\d" != \D and "\d\d\d\d\d\d\d\d\d\d\d" == "\d{11}" and "\d{5,11}"
    if re.match(regex,text):    #TODO return None if do not match
                                #TODO \s == (white coracter)space is correct != \S
        print("match")          #TODO Anchor is start with "^" and end with "$" without []
    print(re.fullmatch(regex,text))

def test():
    text = """
    :: #ali# $quera$
    quera a'l'i ali
    quera  
    """
    print(re.sub(r"^\s*|::|:|#|\'|\$|\s*$","",text).replace('\n', ' ').split())

if __name__ == "__main__":
    import re

    test()
    #main()
"""
در رِجِکس دو علامت + و * بسیار پرکاربرد هستند که آشنایی با سازوکار آن‌ها الزامی است. علامت + حاکی از آن است که
 کاراکتر مذکور می‌تواند تا بی‌نهایت بار تکرار شود اما حداقل یک بار می‌باید درج شده باشد و کاراکتر  *
  نیز دقیقاً‌ همین تعریف را دارا است با این تفاوت که چنین کاراکتری می‌تواند همان یک بار هم تکرار نشود.
"""
"""
از دیگر علائم مرتبط با این حوزه می‌توان به 
? اشاره کرد که حاکی از آن است که کاراکتر مذکور می‌باید یا هیچ بار و یا فقط یک بار تکرار شده باشد.
"""