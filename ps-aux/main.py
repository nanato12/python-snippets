import subprocess as sp

def exec_ps(grep_list=[]):
    item_title_list = ["USER", "PID", "%CPU", "%MEM", "SIZE", "RSS", "TTY", "STAT", "START", "TIME", "COMMAND"]
    cmd = 'ps aux'
    if grep_list:
        for grep in grep_list:
            cmd += f" | grep '{grep}'"
    sp_result = sp.Popen(cmd, shell=True, stdout=sp.PIPE)
    stdout_list = sp_result.communicate()[0].decode('utf-8')[:-1].split('\n')
    results = []
    for stdout in stdout_list:
        out_info = {}
        for n, item in enumerate(stdout.split()):
            key = item_title_list[n]
            out_info[key] = item
            if n == len(item_title_list)-1:
                out_info[key] = ' '.join(stdout.split()[n:])
                break
        results.append(out_info)
    return results

if __name__ == "__main__":
    results = exec_ps(['python3', 'bin'])

    for result in results:
        print(result)

    # pidのみ取得
    for result in results:
        print(result['PID'])

    # コマンドのみ取得
    for result in results:
        print(result['COMMAND'])
