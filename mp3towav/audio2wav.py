import os
import shutil
import sys


def call_sox_cmd(input, output):
    cmd = 'sox' + ' ' + input + ' ' + output
    os.system(cmd)


def audio_to_wav_file(audiofile, wavfile):
    call_sox_cmd(audiofile, wavfile)


def audio_to_wav_dir(inputdir, outdir):
    if not os.path.isdir(inputdir):
        print(inputdir + 'is not dir')
        return
    if not os.path.exists(outdir):
        os.makedirs(outdir, exist_ok=True)

    temp_dir = './tempdir'
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir, exist_ok=True)

    deal_with_audio_file_path(inputdir, temp_dir)  # 修改文件

    for root, dirs, files in os.walk(temp_dir, topdown=True):
        for file_name in files:
            portion = os.path.splitext(file_name)
            if portion[1] == ".mp3":
                new_file_name = portion[0] + '.wav'
                call_sox_cmd(os.path.join(root, file_name), os.path.join(outdir, new_file_name))
                new_file_name_lab = portion[0] + '.lab'
                lab = open(os.path.join(out_dir, new_file_name_lab), 'w')

                word = ' '.join(portion[0].split('_'))
                lab.write(word)
                lab.close()

    os.remove(temp_dir)

def deal_with_audio_file_path(indir, out_dir):
    if not os.path.isdir(indir):
        print(indir + 'is not dir')
        return
    if not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)
    for root, dirs, files in os.walk(input_dir, topdown=True):
        for file_name in files:
            if " " in file_name and file_name.endswith('mp3'):
                new_file_name = file_name.replace(' ', '_')
                print(new_file_name)
            else:
                new_file_name = file_name
            shutil.copyfile(os.path.join(root, file_name), os.path.join(out_dir, new_file_name))


if __name__ == '__main__':
    input_dir = sys.argv[1]
    print('mp3dir:' + input_dir)
    out_dir = sys.argv[2]
    audio_to_wav_dir(input_dir, out_dir)
