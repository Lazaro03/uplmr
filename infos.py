from pyobigram.utils import sizeof_fmt,nice_time
import datetime
import time
import os

def text_progres(index,max):
	try:
		if max<1:
			max += 1
		porcent = index / max
		porcent *= 100
		porcent = round(porcent)
		make_text = ''
		index_make = 1
		make_text += '\n['
		while(index_make<21):
			if porcent >= index_make * 5: make_text+='●'
			else: make_text+='○'
			index_make+=1
		make_text += ']\n'
		return make_text
	except Exception as ex:
			return ''

def porcent(index,max):
    porcent = index / max
    porcent *= 100
    porcent = round(porcent)
    return porcent

def createDownloading(filename,totalBits,currentBits,speed,time,tid=''):
    msg = '📥 Descargando 📥\n\n'
    msg+= '🧩Nombre: ' + str(filename)+'\n'
    msg+= '🗂Tamaño:: ' + str(sizeof_fmt(totalBits))+'\n'
    msg+= '🍁Descargado: ' + str(sizeof_fmt(currentBits))+'\n'
    msg+= '📶Velocidad: ' + str(sizeof_fmt(speed))+'/s\n'
    msg+= '🕐Tiempo: ' + str(datetime.timedelta(seconds=int(time))) +'\n\n'

    msg = '📥 Descargando 📥\n\n'
    msg += '🧩Nombre: '+filename+'\n'
    msg += text_progres(currentBits,totalBits)+'\n'
    msg += '🍂Porcentaje: '+str(porcent(currentBits,totalBits))+'%\n\n'
    msg += '🗂Tamaño Total: '+sizeof_fmt(totalBits)+'\n\n'
    msg += '📥Descargado: '+sizeof_fmt(currentBits)+'\n\n'
    msg += '📶Velocidad: '+sizeof_fmt(speed)+'/s\n\n'
    msg += '⏳Completado en: '+str(datetime.timedelta(seconds=int(time)))+'s\n\n'

    if tid!='':
        msg+= '/cancel_' + tid
    return msg
def createUploading(filename,totalBits,currentBits,speed,time,originalname=''):
    msg = '🚀 Subiendo 🚀\n\n'
    msg+= '🧩Nombre: ' + str(filename)+'\n'
    if originalname!='':
        msg = str(msg).replace(filename,originalname)
        msg+= '🗽Subiendo: ' + str(filename)+'\n'
    msg+= '🗂Tamaño Total: ' + str(sizeof_fmt(totalBits))+'\n'
    msg+= '📚Subido: ' + str(sizeof_fmt(currentBits))+'\n'
    msg+= '📶Velocidad: ' + str(sizeof_fmt(speed))+'/s\n'
    msg+= '⏳Tiempo: ' + str(datetime.timedelta(seconds=int(time))) +'\n'

    msg = '🚀 Subiendo 🚀\n\n'
    msg += '🧩Nombre: '+filename+'\n'
    if originalname!='':
        msg = str(msg).replace(filename,originalname)
        msg+= '🌵Nombre: ' + str(filename)+'\n'
    msg += text_progres(currentBits,totalBits)+'\n'
    msg += '🍂Porcentaje: '+str(porcent(currentBits,totalBits))+'%\n\n'
    msg += '🗂Tamaño: '+sizeof_fmt(totalBits)+'\n\n'
    msg += '📤Subido: '+sizeof_fmt(currentBits)+'\n\n'
    msg += '📶Velocidad: '+sizeof_fmt(speed)+'/s\n\n'
    msg += '⏳Restante: '+str(datetime.timedelta(seconds=int(time)))+'s\n\n'

    return msg
def createCompresing(filename,filesize,splitsize):
    msg = '📚Comprimiendo... \n\n'
    msg+= '🧩Nombre: ' + str(filename)+'\n'
    msg+= '🗂Tamaño Total: ' + str(sizeof_fmt(filesize))+'\n'
    msg+= '🗃Tamaño Partes: ' + str(sizeof_fmt(splitsize))+'\n'
    msg+= '✏️Cantidad Partes: ' + str(round(int(filesize/splitsize)+1,1))+'\n\n'
    return msg
def createFinishUploading(filename,filesize,split_size,current,count,findex):
    msg = '✅Finalizado✅\n\n'
    msg+= '🧩Nombre: ' + str(filename)+'\n'
    msg+= '🗂Tamaño Total: ' + str(sizeof_fmt(filesize))+'\n'
    msg+= '📚Partes Subidas: ' + str(current) + '/' + str(count) +'\n\n'
    msg+= '🗃Ver tu Archivo aqui: https://eduvirtual.uho.edu.cu/admin/tool/lp/user_evidence_list.php\n'
    msg+= 'ℹ️  Tenga en cuenta los otros susuarios y no elimine nada que no sea de usted ℹ️\n'
    return msg

def createFileMsg(filename,files):
    import urllib
    if len(files)>0:
        msg= '<b>🖇Enlaces🖇</b>\n'
        for f in files:
            url = urllib.parse.unquote(f['directurl'],encoding='utf-8', errors='replace')
            #msg+= '<a href="'+f['url']+'">🔗' + f['name'] + '🔗</a>'
            msg+= "<a href='"+url+"'>🔗"+f['name']+'🔗</a>\n'
        return msg
    return ''

def createFilesMsg(evfiles):
    msg = '🗄Archivos🗄 ('+str(len(evfiles))+') 📑\n\n'
    i = 0
    for f in evfiles:
            try:
                fextarray = str(f['files'][0]['name']).split('.')
                fext = ''
                if len(fextarray)>=3:
                    fext = '.'+fextarray[-2]
                else:
                    fext = '.'+fextarray[-1]
                fname = f['name'] + fext
                msg+= '/txt_'+ str(i) + ' /del_'+ str(i) + '\n' + fname +'\n\n'
                i+=1
            except:pass
    return msg
def createStat(username,userdata,isadmin):
    from pyobigram.utils import sizeof_fmt
    msg = '⚙️Condiguraciones⚙️\n\n'
    msg+= '🧧 Nombre: @' + str(username)+'\n'
    msg+= '👤 User: ' + str(userdata['moodle_user'])+'\n'
    msg+= '🎲 Password: ' + str(userdata['moodle_password'])+'\n'
    msg+= '📡 Host: ' + str(userdata['moodle_host'])+'\n'
    if userdata['cloudtype'] == 'moodle':
        msg+= '🆔 RepoID: ' + str(userdata['moodle_repo_id'])+'\n'
    msg+= '🧲 CloudType: ' + str(userdata['cloudtype'])+'\n'
    msg+= '🍁 UpType: ' + str(userdata['uploadtype'])+'\n'
    if userdata['cloudtype'] == 'cloud':
        msg+= '☄️Dir: /' + str(userdata['dir'])+'\n'
    msg+= '📚 Tamaño de Zips : ' + sizeof_fmt(userdata['zips']*1024*1024) + '\n\n'
    msgAdmin = 'No ❌'
    if isadmin:
        msgAdmin = 'Si ✅'
    msg+= '🦾Admin : ' + msgAdmin + '\n'
    proxy = 'Desactivado ❌'
    if userdata['proxy'] !='':
       proxy = 'Activado ✅'
    tokenize = 'NO 😕'
    if userdata['tokenize']!=0:
       tokenize = 'SI 🤩'
    msg+= '🔌Proxy : ' + proxy + '\n'
    msg+= '🔮Tokenize : ' + tokenize + '\n\n'
    return msg
