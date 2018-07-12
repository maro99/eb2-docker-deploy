#!/usr/bin/env python
import os
import subprocess



import argparse

# 사용자가 입력한 mode

def mode_function(mode):
    if mode =='base':
        build_base()
    elif mode == 'local':
        raise NotImplementedError( 'build_local not implemented')
    else:
        raise ValueError(f'{MODES}예 속하는 모드만 가능합니다.')


def build_base():
    try:
        # pipenv lock으로 requirements.txt.생성
        subprocess.call('pipenv lock --requirements > requirements.txt',shell=True)
        # docker.build
        subprocess.call('docker build -t eb-docker:base -f Dockerfile.base .', shell=True)

    finally:
        # 끝난 후 requirements,txt파일 삭제.
        os.remove('requirements.txt')

def build_local():
    try:
        # pipenv lock으로 requirements.txt.생성
        subprocess.call('pipenv lock --requirements > requirements.txt',shell=True)
        # docker.build
        subprocess.call('docker build -t eb-docker:local -f Dockerfile.local .', shell=True)

    finally:
        # 끝난 후 requirements,txt파일 삭제.
        os.remove('requirements.txt')




if __name__ =='__main__':


    MODES = ['base','local']

    # ./build.py --mode <mode>
    # ./build.py -m<mode>
    parser = argparse.ArgumentParser()
    parser.add_argument('-m','--mode',
                        help ='Docker build mode[base,locall]'
                        )

    args = parser.parse_args()


    # 모듈 호출에 옵션으로 mode를 전달한 경우
    if args.mode:
        mode = args.mode.strip().lower()

    #옵션을 입력하지 않았을 경우(./build/.py)
    else:
        while True:
            print('Select mode')
            print('1. base')
            print('2. local')
            selected_mode = input('Choice: ')

            try:
                mode_index = int(selected_mode)-1
                mode = MODES[mode_index]
            except IndexError:
                print('1~2번을 입력하세요')

    # 선택된 mode에 해당하는 함수를 실행
    mode_function(mode)