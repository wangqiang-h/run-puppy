import openai

input = [
    {
        "key": "天气",
        "type": "分类变量",
        "available_values": ["晴朗", "阴天", "雨天", "下雪等"],
        "cn_description": "不同天气对小狗情绪的影响"
    },
    {
        "key": "用户登陆",
        "type": "布尔型变量",
        "available_values": ["已登陆", "未登陆"],
        "cn_description": "用户是否登陆陪伴小狗"
    },
    {
        "key": "运动里程",
        "type": "数值型变量",
        "available_values": ["1.2 km", "0 km", "5 km", "10 km"],
        "cn_description": "用户和小狗陪跑的累计里程"
    },
    {
        "key": "用户给狗消费",
        "type": "数值型变量",
        "available_values": ["0 元", "10 元", "30 元"],
        "cn_description": "用户用于购买小狗用品的金额"
    },
    {
        "key": "用户交友互动",
        "type": "布尔型变量",
        "available_values": ["是", "否"],
        "cn_description": "用户是否和其他用户互动交友"
    },
    {
        "key": "用户互动时长",
        "type": "数值型变量",
        "available_values": ["30 分钟", "2 小时"],
        "cn_description": "用户陪伴小狗的时长"
    },
    {
        "key": "用户点赞或互动次数",
        "type": "数值型变量",
        "available_values": ["0 次", "5 次"],
        "cn_description": "用户对小狗或其他用户点赞互动次数"
    },
    {
        "key": "用户喂食行为",
        "type": "布尔型变量",
        "available_values": ["是", "否"],
        "cn_description": "用户是否喂食小狗"
    }
]

output = [
    {
        "key": "小狗情绪",
        "type": "分类变量",
        "available_values": ["高兴", "悲伤", "兴奋", "焦虑", "孤单等"],
        "cn_description": "小狗表现的情绪状态"
    },
    {
        "key": "小狗体力状态",
        "type": "分类变量",
        "available_values": ["活力充沛", "一般", "疲倦等"],
        "cn_description": "根据运动、休息情况判断的状态"
    },
    {
        "key": "小狗健康状态",
        "type": "分类变量",
        "available_values": ["健康", "轻微不适", "生病等"],
        "cn_description": "根据用户喂养消费情况判定健康程度"
    },
    {
        "key": "小狗社交满意度",
        "type": "分类变量",
        "available_values": ["孤单", "一般", "满足等"],
        "cn_description": "根据用户交友互动情况决定"
    }
]

status = {"天气": "晴朗", "运动里程": "5 km", "用户喂食行为": "是", "用户给狗消费": "30 元", "用户交友互动": "是",
          "用户点赞或互动次数": "5 次", "用户登陆": "已登陆", "用户互动时长": "2 小时"}

prompt = f"""
你是一个AI助手，负责分析用户和小狗的互动数据，并给出小狗的情绪状态和健康状态。请根据以下输入数据，输出小狗的情绪状态、体力状态、健康状态和社交满意度。
可用的输入：{input}
输出： {output}

备注：
1. 用户登陆次数增加，提升小狗的正面情绪和状态
2. 用户给狗消费和互动增加，提升小狗的正面情绪和状态

当前状态为{status} , 请输出小狗的情绪状态、体力状态、健康状态和社交满意度，格式为json
"""

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.0
)

print(response.choices[0].message.content)
# [{'key': '小狗情绪', 'value': '高兴'}, {'key': '小狗体力状态', 'value': '活力充沛'},
# {'key': '小狗健康状态', 'value': '健康'}, {'key': '小狗社交满意度', 'value': '满足'}]
