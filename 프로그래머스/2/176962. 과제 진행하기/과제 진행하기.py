def solution(plans):
    # 시작 시간을 분 단위로 변환하여 추가
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(":"))
        plans[i].append(60 * h + m)
        plans[i][2] = int(plans[i][2])
    
    # 시작 시간 기준으로 정렬
    sorted_plans = sorted(plans, key=lambda x: x[3])
    
    current_time = sorted_plans[0][3] # 첫 번째 과제 시작 시간으로 초기화
    finished_hw = []
    paused_hw = []
    
    for i in range(len(sorted_plans)):
        if i < len(sorted_plans) - 1:
            next_homework_t = sorted_plans[i + 1][3]
        else:
            next_homework_t = float('inf')  # 마지막 과제 이후에는 무한대 시간
        
        done_time = sorted_plans[i][3] + sorted_plans[i][2]
        
        if done_time > next_homework_t:
            # 현재 과제를 중단하고 다음 과제를 시작
            sorted_plans[i][2] = (done_time - next_homework_t)
            paused_hw.append(sorted_plans[i])
            current_time = next_homework_t
        else:
            # 과제를 완료한 경우
            finished_hw.append(sorted_plans[i][0])
            current_time = done_time
            
            # 멈춘 과제 처리
            while paused_hw and current_time < next_homework_t:
                hw = paused_hw.pop()
                done_time = current_time + hw[2]
                
                if done_time > next_homework_t:
                    # 멈춘 과제를 다시 멈추고 다음 과제를 시작
                    hw[2] = done_time - next_homework_t
                    paused_hw.append(hw)
                    current_time = next_homework_t
                else:
                    # 멈춘 과제를 완료
                    finished_hw.append(hw[0])
                    current_time = done_time
    
    return finished_hw
