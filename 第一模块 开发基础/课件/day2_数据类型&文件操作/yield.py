
import os, time

def logger(file_name, channel = 'file'):



    count = 1

    # current_path_file = os.getcwd() + '\\' + file_name
    #
    # if not os.path.exists(current_path_file):
    #     f = open(current_path_file, "w", encoding="utf-8")
    #     f.close()
    if not os.path.exists(file_name):
        f = open(file_name,"w",encoding="utf-8")
        f.close()

    f = open(file_name, "a+", encoding="utf-8")  # 放在这，以后每次调用 ， 不用重新打开文件 了

    log_content = ""

    while True:

        if count == 1:
            log_content = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " [%s] " % (
                count) + "test log db backup %s" % (count)
            count += 1
        sign = yield log_content
        if sign:
            log_content = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " [%s] " % (count) + sign
            count += 1
        else:
            log_content = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " [%s] " % (
                count) + "test log db backup %s" % (count)
            count += 1

        f.write(log_content + "\n")


log = logger("temp_log")
log.__next__()
log.send("test hahah")
log.send("shut donw.")