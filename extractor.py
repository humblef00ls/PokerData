
import pandas as pd
from os import walk

filedir = './Final_Data/'

flx = next(walk(filedir))[1]


csvs = []

for f in flx:
    try:
        filenames = ['hdb','hroster']
        inner_filenames = next(walk(filedir+f+'/pdb/'), (None, None, []))[2]  
        # print(filenames,":",inner_filenames)
        
        datax = []
        for filer in inner_filenames:
            # print('at file',filer)
            with open(filedir+f+'/pdb/'+filer) as fx:
                lines = fx.readlines()
                for line in lines:

                    lx = line.split('\t')[0]
                    ndat = list(filter(lambda x: x != '',lx.split(' ')))
                    if ndat[0] == '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00':
                        break
                    if ndat[-1] == '\n':
                        continue

                    ndat[-1] = ndat[-1].strip('\n')

                    ndat[2:8] = []
                    ndat[3] = int(ndat[4]) - int(ndat[3])
                    ndat[4] = ndat[5]+ ndat[6]
                    ndat[5] = ndat[5][0] + ndat[6][0]
                    ndat[6] = ''
                    datax.append(ndat)



        dataxmap = {}
        with open(filedir+f+'/hdb') as fx:
            lines = fx.readlines()
            for line in lines:
                lx = line.split('\t')[0]
                ndat = list(filter(lambda x: x != '',lx.split(' ')))
                ndat[-1] = ndat[-1].strip('\n')
                ndat[1:8] = []
                ndat[1] = ''.join(ndat[1:])
                ndat[2:] = []
                dataxmap[ndat[0]] = ndat[1]


        dfx = pd.DataFrame(data=datax,columns=['player_name','hand_id','starting_bankroll','net_earning','player_cards','play_cards_value','community_cards'])

        dfx['community_cards'] = dfx.apply(lambda x: dataxmap[x['hand_id']],axis=1)
        csvs.append(dfx)
    except:
        print(f,' FAILED')
        continue
    print(f,' PASSED')


pd.concat(csvs).to_csv('./out/extractedBDF.csv',index=False)