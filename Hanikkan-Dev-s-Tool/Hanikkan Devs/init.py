from icon import iconPrint
from complementos import ExMsgBomb, MsgBomb

iconPrint()
print("[1] ExMsgBomb      [2] MsgBomb")
print("[3] ExPhishing     [4] Phishing")
option = input(">>>")

if int(option) == 1:
    ExMsgBomb()
elif int(option) == 2:
    MsgBomb()
# elif option == 3:

# elif option == 4:
