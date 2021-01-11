#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Autor: Víctor García Carrera victorgarcia@correo.ugr.es
	Clave publica pubkey de 200 números. Ciframos mensajes de 200 bits haciendo
	el prod escalar entre pubkey y el mensaje (visto como vectores). Ej: Pubkey 3,5,7,9,11...
	Mensaje: 01001  Cifrado: 5+11
	"""
# PARA P3 VEMOS QUE ESOS PROBLEMAS COMPLEJOS, CON ALGO DE INFO ADICIONAL, SE RESUELVEN MUY FACIL (factorizacion CON PHI(N))

""" Similar al PROBLEMA DE LA MOCHILA, problema NP-completo
	elegir sucesion y0,y1,y2...,y199
	tq
IMP y0+y1+...+yk < yk+1		IMP

ALGORITMO POSIBLE:
CONDICIONES:
	n > y0+y1+...+yk		Creo que el suyo es nextPrime(suma)
	u: mcd(u,n) = 1
ALG:
	x0 = u*y0 mod n
	x1 = u*y1 mod 
	...
	xn = u*y199 mod n

	m = x1+x2+...+x199
	A PARTIR DE m calculado 
	m*u^-1 mod n = x1*u^-1 +...+xn*u^-1
				 = y1+y2+...+yn
	ya solo queda pasar a binario y dar la vuelta para descodificar

Ejemplo:
	LISTA= 1 2 5 9 21 40
	Elegimos 28
	min(LISTA) +prox a 28: 21
	28-21 = 7
	REPETIMOS: 5
	7-5=2
	...
	2,5,21
Jesus cogió una lista con estas condiciones

"""

import sys
from math import *
from random import *
from fractions import *

clave_publica = [2548399104670841171561012677845109116259615715345168733976355, 1882922120823701792038101171007893027474825423849132510758583, 551968153129423032992278157333460849905244840857060064323039, 1103936306258846065984556314666921699810489681714120128646078, 2207872612517692131969112629333843399620979363428240257292156, 1201869136517403712854301073985361594197552720015275557390185, 2403738273034807425708602147970723188395105440030551114780370, 1593600457551634300333280111259121171745804873219897272366613, 3187200915103268600666560222518242343491609746439794544733226, 3160525741688556650249196260354159481938813486038384132272325, 3107175394859132749414468336025993758833220965235563307350523, 3000474701200284947745012487369662312622035923629921657506919, 2787073313882589344406100790056999420199665840418638357819711, 2360270539247198137728277395431673635354925673996071758445295, 1506664989976415724372630606181022065665445341150938559696463, 3013329979952831448745261212362044131330890682301877119392926, 2812783871387682346406598240041763057617375357762549281591725, 2411691654257384141729272295401200910190344708683893605989323, 1609507219996787732374620406120076615336283410526582254784519, 5138351475594913665316627557828025628160814211959552374911, 10276702951189827330633255115656051256321628423919104749822, 20553405902379654661266510231312102512643256847838209499644, 41106811804759309322533020462624205025286513695676418999288, 82213623609518618645066040925248410050573027391352837998576, 164427247219037237290132081850496820101146054782705675997152, 328854494438074474580264163700993640202292109565411351994304, 657708988876148949160528327401987280404584219130822703988608, 1315417977752297898321056654803974560809168438261645407977216, 2630835955504595796642113309607949121618336876523290815954432, 2047795822491211042200302434533573038192267746205376674714737, 881715556464441533316680684384820871340129485569548392235347, 1763431112928883066633361368769641742680258971139096784470694, 312986137339785582182798552856958280316111935436988611747261, 625972274679571164365597105713916560632223870873977223494522, 1251944549359142328731194211427833121264447741747954446989044, 2503889098718284657462388422855666242528895483495908893978088, 1793902108918588763840852661029007280013384960150612830762049, 373928129319196976597781137375689354982363913460020704329971, 747856258638393953195562274751378709964727826920041408659942, 1495712517276787906391124549502757419929455653840082817319884, 2991425034553575812782249099005514839858911307680165634639768, 2768973980589171074480574013328704474673416608519126312085409, 2324071872660361597877223841975083744302427210197047666976691, 1434267656802742644670523499267842283560448413552890376759255, 2868535313605485289341046998535684567120896827105780753518510, 2523194538692990027598169812389043929197387647370356549842893, 1832512988867999504112415440095762653350369287899508142491659, 451149889218018457140906695509200101656332568957811327789191, 902299778436036914281813391018400203312665137915622655578382, 1804599556872073828563626782036800406625330275831245311156764, 395323025226167106043329379391275608206254544821285665119401, 790646050452334212086658758782551216412509089642571330238802, 1581292100904668424173317517565102432825018179285142660477604, 3162584201809336848346635035130204865650036358570285320955208, 3111292315100693145609345885578084526255666710299365684716289, 3008708541683405740134767586473843847466927413757526412238451, 2803540994848830929185610988265362489889448820673847867282775, 2393205901179681307287297791848399774734491634506490777371423, 1572535713841382063490671399014474344424577262171776597548719, 3145071427682764126981342798028948688849154524343553195097438, 3076266766847547702878761411375572172653903041845901433000749, 2938657445177114854673598638068819140263400076850597908807371, 2663438801836249158263273091455313075482394146859990860420615, 2113001515154517765442621998228300945920382286878776763647103, 1012126941791054979801319811774276686796358566916348570100079, 2024253883582109959602639623548553373592717133832697140200158, 834631678646239368121355062414781542141028260824189323206189, 1669263357292478736242710124829563084282056521648378646412378, 124650626066976921401496064976800963519707036455552335630629, 249301252133953842802992129953601927039414072911104671261258, 498602504267907685605984259907203854078828145822209342522516, 997205008535815371211968519814407708157656291644418685045032, 1994410017071630742423937039628815416315312583288837370090064, 774943945625280933763949894575305627586219159736469782986001, 1549887891250561867527899789150611255172438319472939565972002, 3099775782501123735055799578301222510344876638945879131944004, 2985675476484266919027674971920119815645347271050553306693881, 2757474864450553286971425759157914426246288535259901656193635, 2301073640383126022858927333633503647448171063678598355193143, 1388271192248271494633930482584682089851936120515991753192159, 2776542384496542989267860965169364179703872241031983506384318, 2339208680475105427451797745656403154363338475222762055574509, 1464541272432230303819671306630481103682270943604319153954891, 2929082544864460607639342613260962207364541887208638307909782, 2644289001210940664194761041839599209684677767576071658625437, 2074701913903900777305597898996873214324949528310938360056747, 935527739289821003527271613311421223605493049780671762919367, 1871055478579642007054543226622842447210986099561343525838734, 528234868641303463025162268563359689377566192281482094483341, 1056469737282606926050324537126719378755132384562964188966682, 2112939474565213852100649074253438757510264769125928377933364, 1012002860612447153117373963824552309976123531410651798672601, 2024005721224894306234747927649104619952247062821303597345202, 834135353931808061385571670615884034860088118801402237496277, 1668270707863616122771143341231768069720176237602804474992554, 122665327209251694458362497781210934395946468364403992790981, 245330654418503388916724995562421868791892936728807985581962, 490661308837006777833449991124843737583785873457615971163924, 981322617674013555666899982249687475167571746915231942327848, 1962645235348027111333799964499374950335143493830463884655696, 711414382178073671583675744316424695625880980819722812117265, 1422828764356147343167351488632849391251761961639445624234530, 2845657528712294686334702977265698782503523923278891248469060, 2477438968906608821585481769849072359962641839716577539743993, 1741001849295237092087039355015819514880877672591950122293859, 268127610072493633090154525349313824717349338342695287393591, 536255220144987266180309050698627649434698676685390574787182, 1072510440289974532360618101397255298869397353370781149574364, 2145020880579949064721236202794510597738794706741562299148728, 1076165672641917578358548220906695990433183406641919641103329, 2152331345283835156717096441813391980866366813283839282206658, 1090786602049689762350268698944458756688327619726473607219189, 2181573204099379524700537397888917513376655239452947214438378, 1149270319680778498317150611095509821708904472064689471682629, 2298540639361556996634301222191019643417808944129378943365258, 1383205190205133442184678259699714081791211881417552929536389, 2766410380410266884369356519399428163582423762835105859072778, 2318944672302553217654788854116531122120441518829006760951429, 1424013256087125884225653523550737039196477030816808564708731, 2848026512174251768451307047101474078392954061633617129417462, 2482176935830522985818689909520622951741502116426029301640797, 1750477783143065420553455634358920698438598226010853646087467, 287079477768150290022987084035516191832790445180502334980807, 574158955536300580045974168071032383665580890361004669961614, 1148317911072601160091948336142064767331161780722009339923228, 2296635822145202320183896672284129534662323561444018679846456, 1379395555772424089283869159885933864280241116046832402498785, 2758791111544848178567738319771867728560482232093664804997570, 2303706134571715806051552454861410252076558457346124652801013, 1393536180625451061019180725040495299108710907851044348407899, 2787072361250902122038361450080990598217421815702088696815798, 2360268633983823692992798715479655991390437624562972436437469, 1506661179449666834901673246276986777736469242284739915680811, 3013322358899333669803346492553973555472938484569479831361622, 2812768629280686788522768800425621905901470962297754705529117, 2411661170043393025961613416168918606758535917754304453864107, 1609446251568805500839302647655512008472665828667403950534087, 5016414619630450594681110628698811900925650493602943874047, 10032829239260901189362221257397623801851300987205887748094, 20065658478521802378724442514795247603702601974411775496188, 40131316957043604757448885029590495207405203948823550992376, 80262633914087209514897770059180990414810407897647101984752, 160525267828174419029795540118361980829620815795294203969504, 321050535656348838059591080236723961659241631590588407939008, 642101071312697676119182160473447923318483263181176815878016, 1284202142625395352238364320946895846636966526362353631756032, 2568404285250790704476728641893791693273933052724707263512064, 1922932481983600857869533099105258181503460098608209569830001, 631988875449221164655142013528191157962514190375214182465875, 1263977750898442329310284027056382315925028380750428364931750, 2527955501796884658620568054112764631850056761500856729863500, 1842034915075788766157211923543204058655707516160508502532873, 470193741633596981230499662404082912267009025479812047871619, 940387483267193962460999324808165824534018050959624095743238, 1880774966534387924921998649616331649068036101919248191486476, 547673844550795298760073114550338093091666196997291425778825, 1095347689101590597520146229100676186183332393994582851557650, 2190695378203181195040292458201352372366664787989165703115300, 1167514667888381838996660731720379539688923569137126449036473, 2335029335776763677993321463440759079377847138274252898072946, 1456182583035546804902718742199192953711288269707300838951765, 2912365166071093609805437484398385907422576539414601677903530, 2610854243624206668526950784114446609800747071987998398612933, 2007832398730432785969977383546568014557088137134791840031739, 801788708942885020856030582410810824069770267428378722869351, 1603577417885770041712061164821621648139540534856757445738702, 3207154835771540083424122329643243296279081069713514891477404, 3200433583025099615764320474604161387513756132585824825760681, 3186991077532218680444716764525997569983106258330444694327235, 3160106066546456809805509344369669934921806509819684431460343, 3106336044574933068527094504057014664799207012798163905726559, 2998796000631885585970264823431704124554008018755122854258991, 2783715912745790620856605462181083044063610030669040751323855, 2353555736973600690629286739679840883082814054496876545453583, 1493235385429220830174649294677356561121222102152548133713039, 2986470770858441660349298589354713122242444204305096267426078, 2759065453198902769614672994027101039440482401768987577658029, 2304254817879824988145421803371876873836558796696770198121931, 1394633547241669425206919422061428542628711586552335439049735, 2789267094483338850413838844122857085257423173104670878099470, 2364658100448697149743753503563388965470440339368136799004813, 1515440112379413748403582822444452725896474671895068640815499, 3030880224758827496807165644888905451792949343790137281630998, 2847884360999674442530407105095485698541492680739069606067869, 2481892633481368333976890025508646192038579354636934254941611, 1749909178444756116869855866334967179032752702432663552689095, 285942268371531682655787547987609153021099398024122148184063, 571884536743063365311575095975218306042198796048244296368126, 1143769073486126730623150191950436612084397592096488592736252, 2287538146972253461246300383900873224168795184192977185472504, 1361200205426526371408676583119421243293184361544749413750881, 2722400410853052742817353166238842486586368723089498827501762, 2230924733188124934550782147795359768128331439337792697809397, 1247973377858269318017640110908394331212256871834380438424667, 2495946755716538636035280221816788662424513743668760876849334, 1778017422915096720986636258951252119804621480496316796504541, 342158757312212890889348333220179034564836954151428635814955, 684317514624425781778696666440358069129673908302857271629910, 1368635029248851563557393332880716138259347816605714543259820, 2737270058497703127114786665761432276518695633211429086519640]
codificacion = {' ':'00000', 'a':'00001', 'b':'00010', 'c':'00011', 'd':'00100', 'e':'00101', 'f':'00110', 'g':'00111', 'h':'01000', 'i':'01001', 'j':'01010', 'k':'01011', 'l':'01100', 'm':'01101', 'n':'01110', 'ñ':'01111', 'o':'10000', 'p':'10001', 'q':'10010', 'r':'10011', 's':'10100', 't':'10101', 'u':'10110', 'v':'10111', 'w':'11000', 'x':'11001', 'y':'11010', 'z':'11011', ',':'11100', '.':'11101', ';':'11110', ':':'11111'}
def codifica(mensaje):
    lista = ''
    for x in mensaje:
    	"""if str(codificacion.get(x)) == None:
    		break"""
        lista = lista + str(codificacion.get(x))
    return lista

# Realiza el producto escalar entre el mensaje codificado y la clave pública
def cifra_aux(lista):
    num = 0
    print(len(lista))
    for i in range(len(lista)):
        num+=int(lista[i])*clave_publica[i]
    return(num)

# Cifrado de un mensaje con más de 40 letras = 200 bits
def cifra(lista):
    k = (len(lista)+199)//200
    lista_dividida = []
    for i in range(k-1):
        aux = lista[200*i:200*(i+1)]
        lista_dividida.append(aux)
    lista_dividida.append(lista[200*(k-1):])
    cifrado = []
    for z in lista_dividida:
        cifrado.append(cifra_aux(z))
    return(cifrado)

# AUX FUNCS -------------------------------------
def read_in():
	if len(sys.argv) != 2:
		print ("Error en los params de entrada")
		exit()
	mensaje = str(sys.argv[1])

	# Mensaje en texto
	return mensaje

# Optimización mejor, coste alg O(log(b))
def potenciamodular (a, b, m):
	aux = 1
	while (b > 0):
		if (b%2 == 1):
			aux = (aux * a) % m
		a = (a**2) % m
		b /= 2

	return aux
#--------------


def main():	
	#rawmensaje = read_in()

	print("--- Cifra mensajes de menos de 200 bits con el prod escalar ---")

	rawmensaje = open("mensaje.txt")
	mensaje = rawmensaje.read()
	print(mensaje)
	mensajeCodif5 = codifica(mensaje)
	print("CODIFICADO:")
	print(mensajeCodif5)
	mensajeCifr = cifra(mensajeCodif5)
	print("CIFRADO:")
	print(mensajeCifr)
	"""result = cifra('10100000010111010101010010000100111100000000000001000100000110100000110000101100111110000001001011100100100011010010000100010000010110110000101000000010110011100000100000100110010100011100000111010010101100100110100101010000100000110100000010001100000010000101011011000010100000000010000101000110100110011111000000000001000001010110000001000000100000001011010010001000010111000001111000000010010101100010100000101111000011001000000100000001000001011100101011100100100100100000000000001000001001010110001010010000001100111010000101111000000000100010010001100101000000000100010000011010000011000010110000000000010111010101001010000010100101101010000000101000010100111101100100100100100001001100101101001110000000100101011000101000000011110011010011010100001011100000000101101001000100001011100000111100000001011001110010010010000001111000000001010000010110100001101000000010100001011001100001000001011100101011100001101001001000000111101000000000101100000000011001001011100000101100000000010000101000000110000001000000111010000000110100000101000000011100101011101000010111000010000000011000010110001100000010001000001')
	print(result)"""



	# PROBABILDIAD DE ERROR = 1/(4^10)

if __name__ == '__main__':
	main()
