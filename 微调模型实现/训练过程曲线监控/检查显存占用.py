import GPUtil

def check_gpu_memory():
    # 设置显存占用的阈值为1MB
    MEMORY_USAGE_THRESHOLD_MB = 1

    # 获取所有可用的GPU信息
    gpus = GPUtil.getGPUs()
    
    # 遍历所有GPU，并打印其显存使用情况
    for gpu in gpus:
        gpu_id = gpu.id
        gpu_name = gpu.name
        total_memory_gb = f"{gpu.memoryTotal / 1024:.2f}GB"  # 将MB转换为GB
        used_memory_gb = f"{gpu.memoryUsed / 1024:.2f}GB"    # 将MB转换为GB
        free_memory_gb = f"{gpu.memoryFree / 1024:.2f}GB"    # 将MB转换为GB
        
        print(f"显卡 {gpu_id} - {gpu_name}:")
        
        # 检查是否有显存占用
        if gpu.memoryUsed > MEMORY_USAGE_THRESHOLD_MB:
            print(f"  警告：当前有一个{used_memory_gb}的后台项目正在占用你的显存。")
        else:
            print("  目前没有程序占用显存。")
        print("")

if __name__ == "__main__":
    check_gpu_memory()
