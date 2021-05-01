import cards_tools
while True:
    # 显示功能菜单
    cards_tools.show_menu()

    action_str = input("请选择希望执行的操作：")
    print("您选择的是【%s】" % action_str)

    # 1,2,3针对名片的操作
    if action_str in ["1", "2", "3"]:  # 使用列表,是一个str类型
      # 新增名片
        if action_str == "1":
            cards_tools.new_card()
        # 显示全部
        elif action_str == "2":
            cards_tools.show_all()
        # 查询名片
        elif action_str == "3":
            cards_tools.search_card()
    elif action_str == "0":
        print("欢迎再次使用【名片管理系统】！")
        break
    else:
        print("您输入的不正确，请重新选择")