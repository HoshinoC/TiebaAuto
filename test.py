import asyncio
import aiotieba as tb
import os

# 从Actions环境变量中获取BDUSS
# 该环境变量配置在"Settings" > "Secrets and variables" > "Actions"
BDUSS = os.environ.get('BDUSS')


async def main():
    if not BDUSS:
        print("错误: 未设置BDUSS环境变量")
        return
    
    async with tb.Client(BDUSS) as client:
        # 获取用户信息
        user = await client.get_self_info()
        user_id = user.user_id
        # 获取用户关注的贴吧
        follow_forums = await client.get_follow_forums(user_id)
        # 遍历用户关注的贴吧，执行签到逻辑
        for forum in follow_forums:
            # print(forum.fid, forum.fname)
            signResult = await client.sign_forum(forum.fname)
            if(signResult):
                print("签到成功")
            else:
                print("签到失败")

if __name__ == "__main__":
    asyncio.run(main())
