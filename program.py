from pygame import *
from random import *
from tkinter import *
from tkinter import filedialog
from math import *

width,height=1200,800 
screen=display.set_mode((width,height)) #setting screen
root=Tk()   
root.withdraw() #hides extra window
font.init() 
arialFont=font.SysFont('Arial',15) #font of the paint project
font.get_fonts()

BLACK=(0,0,0) 
WHITE=(255,255,255)

###loading images
paletteWheel=image.load('images/colourWheel.jpg')
programTitle=image.load('images/kspLogo2.png')
programBackground=image.load('images/programLayout.png')
colDisplayFrame=image.load('images/colDisplay.png')

hover=image.load('tools/hover.png')
hover2=image.load('tools/hover2.png')
hover3=image.load('tools/hover3.png')


bg1=image.load('backgrounds/bg1.png')
bg2=image.load('backgrounds/bg2.png')
bg3=image.load('backgrounds/bg3.png')
bg4=image.load('backgrounds/bg4.png')
bg5=image.load('backgrounds/bg5.png')
bg0T=image.load('backgrounds/bg0T.png')
bg1T=image.load('backgrounds/bg1T.png')
bg2T=image.load('backgrounds/bg2T.png')
bg3T=image.load('backgrounds/bg3T.png')
bg4T=image.load('backgrounds/bg4T.png')
bg5T=image.load('backgrounds/bg5T.png')


stamp1=image.load('stamps/stamp1.png')
stamp2=image.load('stamps/stamp2.png')
stamp3=image.load('stamps/stamp3.png')
stamp4=image.load('stamps/stamp4.png')
stamp5=image.load('stamps/stamp5.png')
stamp6=image.load('stamps/stamp6.png')
stamp7=image.load('stamps/stamp7.png')
stamp8=image.load('stamps/stamp8.png')

stamp1T=image.load('stamps/stamp1T.png')
stamp2T=image.load('stamps/stamp2T.png')
stamp3T=image.load('stamps/stamp3T.png')
stamp4T=image.load('stamps/stamp4T.png')
stamp5T=image.load('stamps/stamp5T.png')
stamp6T=image.load('stamps/stamp6T.png')
stamp7T=image.load('stamps/stamp7T.png')
stamp8T=image.load('stamps/stamp8T.png')

jeb1=image.load('extras/jebediahView1.png')
jeb2=image.load('extras/jebediahView2.png')

pencilRest=image.load('tools/pencilRest.png')
eraserRest=image.load('tools/eraserRest.png')
sprayRest=image.load('tools/sprayRest.png')
shapeRest=image.load('tools/shapeRest.png')
lineRest=image.load('tools/lineRest.png')
rectRest=image.load('tools/rectRest.png')
brushRest=image.load('tools/brushRest.png')
undoRest=image.load('tools/undoRest.png')
redoRest=image.load('tools/redoRest.png')
openRest=image.load('tools/openRest.png')
saveRest=image.load('tools/saveRest.png')
rectRest=image.load('tools/rectRest.png')
eliRest=image.load('tools/eliRest.png')
rectFRest=image.load('tools/rectFRest.png')
eliFRest=image.load('tools/eliFRest.png')
leftRest=image.load('tools/leftRest.png')
rightRest=image.load('tools/rightRest.png')

pencilUse=image.load('tools/pencilUse.png')
eraserUse=image.load('tools/eraserUse.png')
sprayUse=image.load('tools/sprayUse.png')
shapeUse=image.load('tools/shapeUse.png')
lineUse=image.load('tools/lineUse.png')
rectUse=image.load('tools/rectUse.png')
brushUse=image.load('tools/brushUse.png')
undoUse=image.load('tools/undoUse.png')
redoUse=image.load('tools/redoUse.png')
openUse=image.load('tools/openUse.png')
saveUse=image.load('tools/saveUse.png')
eliUse=image.load('tools/eliUse.png')
rectFUse=image.load('tools/rectFUse.png')
eliFUse=image.load('tools/eliFUse.png')
leftUse=image.load('tools/leftUse.png')
rightUse=image.load('tools/rightUse.png')

#setting default state for each icon
pencilIcon=pencilRest
eraserIcon=eraserRest
sprayIcon=sprayRest
shapeIcon=shapeRest
lineIcon=lineRest
rectIcon=rectRest
brushIcon=brushRest
undoIcon=undoRest
redoIcon=redoRest
openIcon=openRest
saveIcon=saveRest
eliIcon=eliRest
rectFIcon=rectFRest
eliFIcon=eliFRest
leftIcon=leftRest
rightIcon=rightRest

jebIcon=jeb1 

###setting up rect objects
canvasRect=Rect(150,80,900,500)
diaRect=Rect(920,610,185,155)
diaRect2=Rect(920,610,185,155)

pencilRect=Rect(50,600,85,85) 
eraserRect=Rect(50,700,85,85)
sprayRect=Rect(150,600,85,85)
shapeRect=Rect(150,700,85,85)
lineRect=Rect(250,600,85,85)
rectRect=Rect(250,700,85,85)
brushRect=Rect(350,600,85,85)
eliRect=Rect(350,700,85,85)
rectFRect=rectRect
eliFRect=eliRect

undoRect=Rect(50,15,85,50)
redoRect=Rect(150,15,85,50)
openRect=Rect(1065,80,85,85)
saveRect=Rect(1065,180,85,85)

leftRect=Rect(915,15,50,50)
rightRect=Rect(1085,15,50,50)
bgRect=Rect(980,15,90,50)

stampRect=Rect(730,595,175,175)
stamp1Rect=Rect(738,603,75,75)
stamp2Rect=Rect(738,687,75,75)
stamp3Rect=Rect(823,603,75,75)
stamp4Rect=Rect(823,687,75,75)

paletteRect=Rect(510,595,200,200)
colDisplayRect=Rect(460,595,30,200)

toolRect=Rect(50,600,385,185)
topRect=Rect(50,15,385,50)
openSaveRect=Rect(1065,80,85,185)
leftRightRect=Rect(915,15,220,50)

###displaying images
screen.blit(programBackground,(0,0)) 
screen.blit(paletteWheel,paletteRect)
draw.rect(screen,WHITE,canvasRect)

#setting initial values
canvasIn=False
rightClick=False
paletteSel=False
paletteSel1=False
toolSel=False
topSel=False
topSel1=False
openSave=False
openSave1=False
leftRight=False
leftRight1=False
stampSel=False
stampSel1=False
colDisplay=False
opened=False
openChange=False
bgChanged=False
stampDone=False

running=True

endShape=False
pastScreen=False
mxInCanvas=False
lineCopy=False
shapeDone=False
shapeUndoStep=False
bgChange=False

tool='none' #tool selection default is none
action='none' #action selection default is none
omx,omy=0,0 #setting value
tTool=tool #temporary tool for stamps
oTool=tool 
size=5 #default size
col=0,0,0,255 #default colour black
oCol=col
r,g,b,a=0,0,0,0 #default values for rgb and alpha(a)
mx,my=0,0   #default values for mouse pos
sx,sy=0,0   #default value for starting position
empty=screen.subsurface(canvasRect).copy()  #default starting canvas
screenCap=empty     #original canvas 
bg0=empty #empty screen for default background
jebCount=0
jebMulti=1
stampPg='1'
stamp=stamp1 #active stamp is first stamp

colList=[(1,0,0,255),(0,1,0,255),(0,0,1,255),(1,1,0,255),(0,0,0,255)] #first colour on colour history palette
undoList=[empty] #undo when you press undo the most recent item added is blitted
redoList=[empty] #redo when you press redo the most recent item added is blitted
shapeList=[]     #coordinates for the shape tool
bgList=[bg0,bg1,bg2,bg3,bg4,bg5] #list of backgrounds
bgTList=[bg0T,bg1T,bg2T,bg3T,bg4T,bg5T] #list of background thumbnails
toolList=['pencil','eraser','spray','shape','line','rect','brush','eli','open','save'] #list of each tool
toolButton=[pencilRect,eraserRect,sprayRect,shapeRect,lineRect,rectRect,brushRect,eliRect,openRect,saveRect]#list of each tool Rect
iconList=[pencilIcon,eraserIcon,sprayIcon,shapeIcon,lineIcon,rectIcon,brushIcon,eliIcon,openIcon,saveIcon]#list of each icon
iconListRest=[pencilRest,eraserRest,sprayRest,shapeRest,lineRest,rectRest,brushRest,eliRest,openRest,saveRest] #list of icons in rest
iconListUse=[pencilUse,eraserUse,sprayUse,shapeUse,lineUse,rectUse,brushUse,eliUse,openUse,saveUse] #list of icon in use
stampList=[stamp1,stamp2,stamp3,stamp4,stamp5,stamp6,stamp7,stamp8] #list of stamps
stampTList=[stamp1T,stamp2T,stamp3T,stamp4T,stamp5T,stamp6T,stamp7T,stamp8T] #list of stamp thumbnails
diaText=['Pencil in fine details with this', #dialogue box text for line 1
         'Erase your mistakes with tool',
         'Spray paint the canvas with this',
         'Left click to select points,',
         'Draw a line with this tool',
         'Draw an rectangle with this tool,',
         'Draw using a paintbrush with',
         'Draw an ellipse with this tool,',
         'Open an image file',
         'Save an image file as a .png',
         'Undo the latest step',
         'Redo the latest step',
         'Cycle left in the background',
         'Cycle right in the background',
         'Select a colour from within the',
         'Select a colour from the colour',
         'Select a stamp with left click,']
diaText2=['tool',                           #dialogue box text for line 2
         '',
         'tool',
         'then right click to complete',
         '',
         'and right click to switch modes',
         'this tool',
         'and right click to switch modes',
         '',
         '',
         '',
         '',
         'selection',
         'selection',
         'range',
         'history',
         'scroll to change the pg. number']
#more default values
diaDisp=diaText[0]      
diaDisp2=diaText2[0]
diaDone=False
diaChange=True
jebTimerCount=0
#blitting more images
screen.blit(bgTList[1],(955,15,90,50))
screen.blit(bgTList[-1],(1025,15,90,50))
screen.blit(jeb1,(1120,650,175,155))

while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
            
        if evt.type==MOUSEBUTTONDOWN:
            if evt.button==1:
                sx,sy=evt.pos               #starting position of tool
                click=True                  #mouse has been clicked
                print("mouse down")
                
                if paletteRect.collidepoint(mx,my): #to see if user is selecting the colour palette
                    paletteSel=True
                else:
                    paleteSel=False
                if colDisplayRect.collidepoint(mx,my): #to see if user is selecting the colour history palette
                    colDisplay=True
                else:
                    colDisplay=False
                if toolRect.collidepoint(mx,my):    #to see if the user is selecting from tools
                    toolSel=True
                else:
                    toolSel=False
                if topRect.collidepoint(mx,my):     #to see if user is selecting from the top buttons
                    topSel=True
                else:
                    topSel=False
                if openSaveRect.collidepoint(mx,my):#to see if user is selecting from open and save buttons
                    openSave=True
                else:
                    openSave=False
                if leftRightRect.collidepoint(mx,my): #to see if the user is selecting from the left and right buttons
                    leftRight=True
                else:
                    leftRight=False
                if stampRect.collidepoint(mx,my):
                    stampSel=True
                else:
                    stampSel=False
                topSel1=topSel                      #making seperate copies of variables
                openSave1=openSave
                leftRight1=leftRight
                paletteSel1=paletteSel
                stampSel1=stampSel
            if evt.button==3:       #right clicking
                if tool=='shape': #shape tool adding points for each click
                    print(len(shapeList))
                    if len(shapeList)>2: #polygon needs to have at least 3 points
                        shapeDone=True  #booleans for setting values later on 
                        shapeUndoStep=True
                        draw.polygon(screen,col,shapeList,size) 
                        screenCap=screen.subsurface(canvasRect).copy()  #copies the screen
                        screen.blit(screenCap,(canvasRect)) #updating the screen
                ###for dialogue text box
                if tool=='rect':
                    tool='rectF'
                    iconList[5]=rectFUse
                elif tool=='rectF':
                    tool='rect'
                    iconList[5]=rectIcon
                elif tool=='eli':
                    tool='eliF'
                    iconList[7]=eliFUse
                elif tool=='eliF':
                    tool='eli'
                    iconList[7]=eliIcon

            if evt.button==4: #scrolling up
                if stampRect.collidepoint(mx,my): #for stamp page scrolling
                    stampPg='1'     #first stamp page
                else:
                    if size+1<41: #increases thickness
                        size+=1
            if evt.button==5: #scrolling down
                if stampRect.collidepoint(mx,my):
                    stampPg='2'     #second stamp page
                else:
                    if size-1>0: #decreases thickness
                        size-=1


        if evt.type==MOUSEBUTTONUP: #release of the mouse
            if evt.button==1: #to prevent scroll wheel from interfering
                if tool!='shape' and tool!='none' or action=='stamp': #all tools + stamps 
                    if mxInCanvas:   #copying screen if the canvas has been altered
                        fwdScreen=screen.subsurface(canvasRect).copy() #adding the copied screen to the undo list
                        undoList.append(fwdScreen) 
                        mxInCanvas=False
                    
                if paletteRect.collidepoint(mx,my) and paletteSel: 
                    colList.append(col)     #adding colour to the colour history list
                    colList.pop(0)          #removing the oldest colour from history
                if colDisplayRect.collidepoint(mx,my) and colDisplay:
                    colPick=colList.index(col)  #finds colour that needs to be swapped
                    colList[colPick],colList[-1]=colList[-1],colList[colPick] #swapping the colours with the one that colour that is picked

            if tool=='shape' and shapeUndoStep: #removing the undo steps when the shape tool is used
                shapeUndoStep=False
                fwdScreen=screen.subsurface(canvasRect).copy()
                undoList.append(fwdScreen)
                
            if shapeDone or tool!='shape': #setting the list of points for the shape to be nothing when the old shape is finished
                shapeList*=0
                shapeDone=False
                
            if evt.button==1: 
                screen.set_clip(canvasRect)
                if tool=='line' and canvasRect.collidepoint(mx,my): #drawing the actual line in the program
                    screenCap=screen.subsurface(canvasRect).copy()
                    draw.line(screen,col,(sx,sy),(mx,my),size)
                    fwdScreen=screen.subsurface(canvasRect).copy()
                    
                if tool=='shape' and canvasRect.collidepoint(mx,my) and shapeDone==False: 
                    shapeList.append(mouse.get_pos())
                    for term in range(len(shapeList)):    #drawing each vertice of each shape
                        draw.circle(screen,col,shapeList[term],1)
                        print(shapeDone)
                    
                if tool=='rect' and canvasRect.collidepoint(mx,my):   #drawing the rectangle
                    screenCap=screen.subsurface(canvasRect).copy()
                    draw.rect(screen,col,(sx,sy,mx-sx,my-sy),size)
                    draw.rect(screen,col,(sx-round(size/2,1)+1,round(sy-size/2,1)+1,size,size))
                    draw.rect(screen,col,(mx-round(size/2,1),round(my-size/2,1),size,size))
                    draw.rect(screen,col,(mx-round(size/2,1),round(sy-size/2,1)+1,size,size))
                    draw.rect(screen,col,(sx-round(size/2,1)+1,round(my-size/2,1),size,size))
                    screenCap=screen.subsurface(canvasRect).copy()
                    
                if tool=='rectF' and canvasRect.collidepoint(mx,my):   #drawing the filled rectangle
                    screenCap=screen.subsurface(canvasRect).copy()
                    draw.rect(screen,col,(sx,sy,mx-sx,my-sy))
                    screenCap=screen.subsurface(canvasRect).copy()
                    
                if tool=='eli' and canvasRect.collidepoint(mx,my):     #drawing the unfilled ellipse
                    screenCap=screen.subsurface(canvasRect).copy()
                    if size>10:      #setting max size for ellipse tool
                        size=10
                    sxEli=sx
                    syEli=sy
                    wEli=mx-sx
                    hEli=my-sy
                    eliDrawRect=Rect(sxEli,syEli,wEli,hEli)
                    eliDrawRect.normalize()
                    try:
                        draw.ellipse(screen,col,(eliDrawRect),size) #incase where the size of ellipse collides within the walls
                    except:
                        draw.ellipse(screen,col,(eliDrawRect))  
                    screenCap=screen.subsurface(canvasRect).copy()                        
                if tool=='eliF' and canvasRect.collidepoint(mx,my):     #drawing the filled ellipses
                    if size>10:     #setting max size for filled ellipse tool
                        size=10
                    sxEli=sx
                    syEli=sy
                    wEli=mx-sx
                    hEli=my-sy
                    eliDrawRect=Rect(sxEli,syEli,wEli,hEli)
                    eliDrawRect.normalize()
                    try:
                        draw.ellipse(screen,col,(eliDrawRect),size)
                    except:
                        pass
                    screenCap=screen.subsurface(canvasRect).copy()
                    
                if stampSel:                #when stamp is selected, blitting the proper stamps for each page number
                    action='stamp'
                    diaDone=True
                    if stampPg=='1': #determining what stamp is selected
                        if stamp1Rect.collidepoint(mx,my):
                            stamp=stampList[0]
                        if stamp2Rect.collidepoint(mx,my):
                            stamp=stampList[1]
                        if stamp3Rect.collidepoint(mx,my):
                            stamp=stampList[2]
                        if stamp4Rect.collidepoint(mx,my):
                            stamp=stampList[3]
                    if stampPg=='2':   
                        if stamp1Rect.collidepoint(mx,my):
                            stamp=stampList[4]
                        if stamp2Rect.collidepoint(mx,my):
                            stamp=stampList[5]
                        if stamp3Rect.collidepoint(mx,my):
                            stamp=stampList[6]
                        if stamp4Rect.collidepoint(mx,my):
                            stamp=stampList[7]

                if action=='stamp':         #blitting the stamps
                    if mb[0]==1 and canvasRect.collidepoint(mx,my):
                        cw=stamp.get_width()
                        ch=stamp.get_height()
                        screen.blit(stamp,(mx-cw/2,my-ch/2)) #centering the stamps
                screen.set_clip(None)
                    
            if bgChanged:  #when the background is changed
                fwdScreen=screen.subsurface(canvasRect).copy() #added in later codes to undolist
                bgChanged=False
            paletteSel=False 
            print("mouse up")

               
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    
    if mb[0]==1 and canvasRect.collidepoint(mx,my):
        mxInCanvas=True
    if canvasRect.collidepoint(mx,my):
        canvasIn=True   #boolean for the stamps
    else:
        canvasIn=False

###drawing the rectangles and blitting images on screen
    for q in range(len(iconList)):  #connected lists, blitted
        screen.blit(iconList[q],toolButton[q])
    screen.blit(undoIcon,(undoRect))
    screen.blit(redoIcon,(redoRect))
    screen.blit(leftIcon,(leftRect))
    screen.blit(rightIcon,(rightRect))
    screen.blit(jebIcon,(1120,650,175,155)) #jebediah character in bottom right

    draw.rect(screen,WHITE,stampRect)
    draw.rect(screen,WHITE,diaRect)

    if stampPg=='1':
        screen.blit(stampTList[0],(738,603,75,75))  #blitting the stamps page 1
        screen.blit(stampTList[1],(738,687,75,75))
        screen.blit(stampTList[2],(823,603,75,75))
        screen.blit(stampTList[3],(823,687,75,75))

    if stampPg=='2':
        screen.blit(stampTList[4],(738,603,75,75))  #blitting the stamps on page 2
        screen.blit(stampTList[5],(738,687,75,75))
        screen.blit(stampTList[6],(823,603,75,75))
        screen.blit(stampTList[7],(823,687,75,75))

    if openChange: #changing bg list to default values
        bgList=[bg0,bg1,bg2,bg3,bg4,bg5]
        bgTList=[bg0T,bg1T,bg2T,bg3T,bg4T,bg5T]
        screen.blit(bgTList[1],(955,15,90,50)) #default thumbnails for background in the top right corner
        screen.blit(bgTList[-1],(1025,15,90,50))
        screen.blit(bgList[0],canvasRect)
        screen.blit(myPic,(150+distX,80+distY,900,500)) #putting image in the center of canvas 
        redoList*=0 #clearing the list
        redoList.append(bgList[-1])
        undoList*=0
        fwdScreen=screen.subsurface(canvasRect).copy()
        undoList.append(fwdScreen) 
        openChange=False
    if bgChange:
        screen.blit(bgTList[1],(955,15,90,50))
        screen.blit(bgTList[-1],(1025,15,90,50))
        screen.blit(bgList[0],canvasRect)
        bgChange=False
        
                
###hovering over objects
    for q in range(len(toolList)):  #list of each tool and its rect location for hovering
            if toolButton[q].collidepoint(mx,my):
                screen.blit(hover,(toolButton[q]))
    if undoRect.collidepoint(mx,my):    #undo,redo,right,and left arent in a list because they are smaller icons
        screen.blit(hover2,(undoRect))
    if redoRect.collidepoint(mx,my):
        screen.blit(hover2,(redoRect))
    if rightRect.collidepoint(mx,my):
        screen.blit(hover3,(rightRect))
    if leftRect.collidepoint(mx,my):
        screen.blit(hover3,(leftRect))
    
###selecting
    if toolSel:         
        if mb[0]==1:
            for q in range(len(toolList)):      #changing the icon to be what is selected
                if toolButton[q].collidepoint(mx,my):
                    tool=toolList[q]
                    iconList=iconListRest[:]
                    iconList[q]=iconListUse[q]

    if mb[0]==1 and redoRect.collidepoint(mx,my): #special cases for different sied icons
        redoIcon=redoUse
    else:
        redoIcon=redoRest
    if mb[0]==1 and undoRect.collidepoint(mx,my):
        undoIcon=undoUse
    else:
        undoIcon=undoRest
    if mb[0]==1 and leftRect.collidepoint(mx,my):
        leftIcon=leftUse
    else:
        leftIcon=leftRest
    if mb[0]==1 and rightRect.collidepoint(mx,my):
        rightIcon=rightUse
    else:
        rightIcon=rightRest

###using buttons
    if topSel: #to see if the cursor is in the top button range
        if mb[0]==1 and undoRect.collidepoint(mx,my):
            action='undo'
            if len(undoList)>1:         #base canvas cant be deleted
                undone=undoList[-1]     #undo step capture saved
                undoList.pop()          #removing the undo step
                screen.blit(undoList[-1],canvasRect) #putting the previous screencap on canvas
                redoList.append(undone) #adding the removed capture
                pastScreen=True         #current canvas exists in the past
                topSel=False            #setting back to default value
                screenCap=screen.subsurface(canvasRect).copy()
        if mb[0]==1 and redoRect.collidepoint(mx,my):
            action='redo'
            if len(redoList)>1:         #base canvas cant be deleted
                redone=redoList[-1]     #redo step capture saved
                screen.blit(redoList[-1],canvasRect) #putting the redone screencap on canvas
                redoList.pop()          #removing the redo step and
                undoList.append(redone) #adding it to the undo step
                topSel=False            #setting back to default value
                screenCap=screen.subsurface(canvasRect).copy()
                
    if openSave:
        if mb[0]==1 and openRect.collidepoint(mx,my):
            action='open'
            try:
                screen.set_clip(canvasRect)
                fName=filedialog.askopenfilename()
                print(fName)
                myPic=image.load(fName)
                widthPic=myPic.get_width() 
                heightPic=myPic.get_height() #cropping the image below
                if widthPic>900: #if width of image is greater than the canvas size,
                    factorW=widthPic/900    #image is scalled so the width fits on canvas
                    muPic=transform.scale(myPic,(int(widthPic/factorW),int(heightPic/factorW))) 
                    widthPic=myPic.get_width()
                    heightPic=myPic.get_height()
                if heightPic>500: #if height of image is greater than canvas size,
                    factorH=heightPic/500   #image is scalled so the height fits on canvas, 
                    myPic=transform.smoothscale(myPic,(int(widthPic/factorH),int(heightPic/factorH)))
                    widthPic=myPic.get_width()
                    heightPic=myPic.get_height()
                distX=(900-widthPic)/2 #calculating distance to be moved to the right to center
                distY=(500-heightPic)/2 #calculating distance to be moved to down to center
                screen.blit(myPic,(150+distX,80+distY,900,500)) #putting image in the center of canvas
                print('opened',fName)
                screen.set_clip(None)
                openChange=True #booleans for further action in event loop+regular loop
                opened=True
                diaDisp=diaText[8]  #dialogue changed to the index for open
                diaDisp2=diaText2[8]
                diaDone=True
                
            except:
                print('opening error')
                diaDisp=diaText[8]
                diaDisp2=diaText2[8]
                diaDone=True

        if mb[0]==1 and saveRect.collidepoint(mx,my):
            action='save'
            try:
                fName=filedialog.asksaveasfilename(defaultextension='.png') #saving image as .png
                image.save(screen.subsurface(canvasRect).copy(),fName)
                print('saved as',fName)
            except:
                print('saving error')
                diaDisp=diaText[9]
                diaDone=True
    else:
        diaDone=False #if these actions arent completed, then the dialogue to be displayed should be from the regular tools

    if leftRight: #changing backgrounds
        if mb[0]==1 and leftRect.collidepoint(mx,my):  
            bgTList.append(bgTList[0]) #swapping the last with the first backgrounds
            bgTList.pop(0)
            bgList.append(bgList[0])
            bgList.pop(0)
            leftRight=False #booleans for further ifs
            bgChange=True
            bgChanged=True
            action='left' 
        if mb[0]==1 and rightRect.collidepoint(mx,my):
            bgTadd=bgTList[-1] #swapping the first with the last backgrounds
            bgTList.reverse()
            bgTList.append(bgTadd)
            bgTList.reverse()
            bgTList.pop()
            bgadd=bgList[-1]
            bgList.reverse()
            bgList.append(bgadd)
            bgList.reverse()
            bgList.pop()
            leftRight=False
            bgChange=True
            bgChanged=True
            action='right'

###colour picking
    if paletteRect.collidepoint(mx,my) and paletteSel: #selecting colours
        action='col palette'
        if mb[0]==1:
            col=screen.get_at((mx,my))
            r,g,b,a=screen.get_at((mx,my))
            diaDisp=diaText[14]     #dialogue is colour
            diaDisp2=diaText2[14]
            diaDone=True #makes it so tool dialogue will be skipped
    else:
        diaDone=False
        
###displaying colours 
    for rectCol in range(5):
        draw.rect(screen,(colList[rectCol]),(460,755-40*rectCol,30,40)) #from colour history palette

    if colDisplayRect.collidepoint(mx,my) and colDisplay:
        action='col pick'
        if mb[0]==1:
            col=screen.get_at((mx,my))  #setting the colour to be the one chosen in the colour history palette
            diaDone=True
            diaDisp=diaText[15]
            diaDisp2=diaText2[15]

    screen.blit(colDisplayFrame,colDisplayRect) #colour history frame

###spray paint tool
    if tool=='spray':
        sprayX=randint(-size-20,size+20) #random points for the x
        sprayY=randint(-size-20,size+20) #random points for the y
            
        if (sprayX)**2+(sprayY)**2<=2*(size+6)**2: #to see if those random points as coordinates fit inside circle
            sprayX=mx+sprayX #if true, the spray can coordinates will be
            sprayY=my+sprayY #sprayXco and sprayYco

        sprayX2=randint(-size-20,size+20) #same code as above, but with a smaller radius
        sprayY2=randint(-size-20,size+20) 
        if (sprayX2)**2+(sprayY2)**2<=2*(size+3)**2: 
            sprayX2=mx+sprayX2 
            sprayY2=my+sprayY2 

        sprayX3=randint(-size-20,size+20)  #same code as above, but with an even smaller radius
        sprayY3=randint(-size-20,size+20)
        
        if (sprayX3)**2+(sprayY3)**2<=2*(size)**2: 
            sprayX3=mx+sprayX3 
            sprayY3=my+sprayY3 

###size of tool
    if tool=='pencil': #setting maximum sizes for pencil
        if size>5:
            size=5
    if tool=='eli' or tool=='eliF' or tool=='shape': #and for ellipse and shape tools
        if size>10:
            size=10

    tTool=tool #temporary tool saved for when the tool is set to none to make the stamps not have tools underneath them
    if action=='stamp':
        tTool=tool
        tool='none'
        screen.set_clip(canvasRect)
        screen.blit(undoList[-1],canvasRect)    #whole block is a preview of where the stamp is/stamp follows cursor
        cw=stamp.get_width()
        ch=stamp.get_height()
        screen.blit(stamp,(mx-cw/2,my-ch/2))    #centering the stamp    
        screen.set_clip(None)
        stampDone=True
    
    if toolRect.collidepoint(mx,my) and mb[0]==1 or col!=oCol or colDisplay: #checks to see if any tools/actions/buttons are used
        if action!='none': #stops using the stamp if new tool/action/col is picked
            action='none'
            screen.blit(undoList[-1],canvasRect) 
        
###using tool
    if canvasRect.collidepoint(mx,my) and mb[0]==1:     
        screen.set_clip(canvasRect)
        if tool=='pencil':          #pencil tool
            draw.line(screen,col,(omx,omy),(mx,my),size)
            
        if tool=='eraser':          #eraser tool
            dx=mx-omx
            dy=my-omy
            hyp=sqrt(dx**2+dy**2)
            if hyp%1!=0:
                hyp+=0.5
            for i in range(0,int(hyp)):
                dotx=int(omx-size//2+i*dx/hyp)
                doty=int(omy-size//2+i*dy/hyp)
                screen.blit(bgList[0],(dotx,doty,size*2,size*2),(dotx-150,doty-80,size*2,size*2)) #draws the background image in a square on top of the image
                
        if tool=='spray':   #spray paint tool
            draw.circle(screen,col,(sprayX,sprayY),0) #outer circle
            draw.circle(screen,col,(sprayX2,sprayY2),0) #middle circle
            draw.circle(screen,col,(sprayX3,sprayY3),0) #inner circle
            
        if tool=='line': #preview of line tool
            screen.blit(undoList[-1],canvasRect)
            draw.line(screen,col,(sx,sy),(mx,my),size)
            
        if tool=='rect': #preview of rectangle tool
            screen.blit(undoList[-1],canvasRect)
            draw.rect(screen,col,(sx,sy,mx-sx,my-sy),size)
            draw.rect(screen,col,(sx-round(size/2,1)+1,round(sy-size/2,1)+1,size,size))
            draw.rect(screen,col,(mx-round(size/2,1),round(my-size/2,1),size,size))
            draw.rect(screen,col,(mx-round(size/2,1),round(sy-size/2,1)+1,size,size))
            draw.rect(screen,col,(sx-round(size/2,1)+1,round(my-size/2,1),size,size))
         
        if tool=='brush':
            if omx!=mx or omy!=my:
                dx=mx-omx
                dy=my-omy
                hyp=sqrt(dx**2+dy**2)
                if hyp%1!=0:
                    hyp+=0.5
                draw.circle(screen,col,(mx,my),size)
                for i in range(0,int(hyp),1):
                    dotx=int(omx+i*dx/hyp)
                    doty=int(omy+i*dy/hyp)
                    draw.circle(screen,col,(dotx,doty),size)
        
        if tool=='eli': #preview of ellipse tool
            screen.blit(undoList[-1],canvasRect)
            sxEli=sx
            syEli=sy
            wEli=mx-sx
            hEli=my-sy
            eliDrawRect=Rect(sxEli,syEli,wEli,hEli)
            eliDrawRect.normalize()
            print(eliDrawRect,size)
            try:
                draw.ellipse(screen,col,(eliDrawRect),size)
            except:
                draw.ellipse(screen,col,(eliDrawRect))
                
        if tool=='rectF': #preview of filled rectangle tool
            screen.blit(undoList[-1],canvasRect)
            draw.rect(screen,col,(sx,sy,mx-sx,my-sy))
            
        if tool=='eliF':  #preview of filled ellipse tool
            screen.blit(undoList[-1],canvasRect)
            sxEli=sx
            syEli=sy
            wEli=mx-sx
            hEli=my-sy
            eliDrawRect=Rect(sxEli,syEli,wEli,hEli)
            eliDrawRect.normalize()
            print(eliDrawRect)
            try:
                draw.ellipse(screen,col,(eliDrawRect))
            except:
                pass
            screenCap=screen.subsurface(canvasRect).copy()

        if pastScreen: #if there is drawing on the canvas when it is done in the past/undo steps
            redoList*=0 #clearing the list
            redoList.append(bgList[-1])
            pastScreen=False
        screen.set_clip(None)

##blitting final information
    toolWord='Tool: '+tool.upper()      #setting up the pregenerated text with the dynamic values (size,mx and my,tool,action)
    actionWord='Latest Action: '+action.upper()
    sizeWord='Size: '+str(size)+' (scroll to change size)'
    posWord='Position: '+str(mx)+','+str(my)
    
    sizePic=arialFont.render(sizeWord,True,(BLACK)) #rendering and blitting each dialogue + texts in the text box
    screen.blit(sizePic,(925,660,185,155))
    diaPic=arialFont.render(diaDisp,True,(BLACK))
    screen.blit(diaPic,(925,675+20,185,155))
    diaPic2=arialFont.render(diaDisp2,True,(BLACK))
    screen.blit(diaPic2,(925,690+20,185,155))
    toolPic=arialFont.render(toolWord,True,(BLACK))
    screen.blit(toolPic,(925,615,185,155))
    actionPic=arialFont.render(actionWord,True,(BLACK))
    screen.blit(actionPic,(925,635,185,155))
    posPic=arialFont.render(posWord,True,(BLACK))
    screen.blit(posPic,(925,675,185,155))
    
    display.flip()

    if stampDone:   #setting the tool back to its original value, before using the stamp tool
        tool=tTool
        stampDone=False
    toolSel=False
    omx=mx  #updating tools with the new tools
    omy=my
    oTool=tool
    oCol=col
    oDiaDisp=diaDisp
    if diaDone!=True:
        if topSel1 or openSave1 or leftRight1 or paletteSel1 or colDisplay or stampSel1: #dialogue box is the text from before
            if action=='open':
                diaDisp=diaText[8]
                diaDisp2=diaText2[8]
            if action=='save':
                diaDisp=diaText[9]
                diaDisp2=diaText2[9]
            if action=='undo':
                diaDisp=diaText[10]
                diaDisp2=diaText2[10]
            if action=='redo':
                diaDisp=diaText[11]
                diaDisp2=diaText2[11]
            if action=='left':
                diaDisp=diaText[12]
                diaDisp2=diaText2[12]
            if action=='right':
                diaDisp=diaText[13]
                diaDisp2=diaText2[13]
            if action=='stamp':
                diaDisp=diaText[16]
                diaDisp2=diaText2[16]
            
        else:
            for x in range(len(toolList)):  #dialogue is the tools
                if tool==toolList[x]:
                    diaDisp=diaText[x]
                    diaDisp2=diaText2[x]
    if bgChanged:   #when you change the background undo and redo are reset *new image
        undoList*=0
        undoList.append(bgList[0])
        redoList*=0
        redoList.append(bgList[0])
        
    if oDiaDisp!=diaDisp: #when the dialogue changes, character is allowed to speak
        diaChange=True
        jebTimerCount=0 #number counter that ranges from positive to negative integers
###counter of time for Jebediah at the bottom right corner 
    jebIcon=jeb1 #default state of Jebediah is closing mouth
    if diaChange: 
        jebTimerCount+=1
    if diaChange:
        jebCount+=jebMulti
        if jebCount>8:
            jebMulti*=-1
        if jebCount<-15:
            jebMulti*=-1
        if jebCount>0:  #when counter is positive character opens their mouth
            jebIcon=jeb1
        else:   #otherwise character is closing their mouth
            jebIcon=jeb2
    if jebTimerCount>200:
        diaChange=False
        jebTimerCount=0
    
quit()
