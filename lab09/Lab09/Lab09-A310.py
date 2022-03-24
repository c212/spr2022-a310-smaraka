from mimetypes import init
import shutil, os

class Firenation:

    def __init__(self, sc = 0, wc = 1):
        self.s_count = sc
        self.w_count = wc

    def mkdir(self, path):
        os.mkdir(path)

    def rmdir(self, path):
        os.rmdir(path)
    
    def rmtree(self, path):
        shutil.rmtree(path)

    def addSoldier(self):
        shutil.copy(r'(Your Path)\Lab09\Pieces\FN-S.txt', rf'(Your Path)\Lab09\Continent\Fire Nation\People\army\Soldier {self.s_count}.txt')
        self.s_count+=1
    
    def backup(self, name):
        shutil.copytree(rf'(Your Path)\Lab09\Continent\{name}', rf'(Your Path)\Lab09\Continent\{name}_{self.w_count}')
        self.w_count+=1

    def moveSoldierHome(self, num):
        shutil.move(rf'(Your Path)\Lab09\Continent\Fire Nation\People\army\Soldier {num}.txt', rf'(Your Path)\Lab09\Continent\Fire Nation\People\Citizens')

    def moveSoldierBack(self, num):
        shutil.move(rf'(Your Path)\Lab09\Continent\Fire Nation\People\Citizens\Soldier {num}.txt', rf'(Your Path)\Lab09\Continent\Fire Nation\People\army')

    def walk(self):
        for folderName, subfolders, filenames in os.walk(r'(Your Path)\Lab09\Continent'):
            print('The current folder is ' + folderName)
            for subfolder in subfolders:
                print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
            for filename in filenames:
                print('FILE INSIDE ' + folderName + ': '+ filename)

            print('')

fn_one = Firenation(6, 7)
# fn_one.addSoldier()
# fn_one.addSoldier()
# fn_one.addSoldier()
# fn_one.addSoldier()
# fn_one.addSoldier()

# fn_one.backup("Fire nation")
# fn_one.backup("Fire nation")

# fn_one.moveSoldierHome(1)
# fn_one.moveSoldierHome(2)
# fn_one.moveSoldierHome(3)

# fn_one.moveSoldierBack(1)
# fn_one.moveSoldierBack(2)
# fn_one.moveSoldierBack(3)

# fn_one.mkdir(r"C:\Users\skmar\Desktop\Lab09\Continent\Fire Nation\People\test")
# fn_one.rmdir(r"C:\Users\skmar\Desktop\Lab09\Continent\Fire Nation\People\test")

# fn_one.rmtree(r"C:\Users\skmar\Desktop\Lab09\Continent\Fire nation_8")
# fn_one.rmtree(r"C:\Users\skmar\Desktop\Lab09\Continent\Fire nation_9")

fn_one.walk()