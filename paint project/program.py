from pygame import *
from random import *
from tkinter import *
from tkinter import filedialog
from math import *

width,height=1200,800
screen=display.set_mode((width,height))
root=Tk()
root.withdraw #hides extra window

RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)
WHITE=(255,255,255)


###loading images
paletteWheel=image.load('images/colourWheel.jfif')
programTitle=image.load('images/kspLogo2.png')
programBackground=image.load('images/programLayout.png')
colDisplayFrame=image.load('images/colDisplay.png')

hover=image.load('tools/hover.png')
hover2=image.load('tools/hover2.png')

pencilRest=image.load('tools/pencilRest.png')
eraserRest=image.load('tools/eraserRest.png')
sprayRest=image.load('tools/sprayRest.png')
shapeRest=image.load('tools/shapeRest.png')
lineRest=image.load('tools/lineRest.png')
rectRest=image.load('tools/bucketRest.png')
brushRest=image.load('tools/brushRest.png')
undoRest=image.load('tools/undoRest.png')
redoRest=image.load('tools/redoRest.png')
openRest=image.load('tools/openRest.png')
saveRest=image.load('tools/saveRest.png')
rectRest=image.load('tools/baseIconNew.png')
eliRest=image.load('tools/baseIconNew.png')

pencilUse=image.load('tools/pencilUse.png')
eraserUse=image.load('tools/eraserUse.png')
sprayUse=image.load('tools/sprayUse.png')
shapeUse=image.load('tools/shapeUse.png')
lineUse=image.load('tools/lineUse.png')
rectUse=image.load('tools/bucketUse.png')
brushUse=image.load('tools/brushUse.png')
undoUse=image.load('tools/undoUse.png')
redoUse=image.load('tools/redoUse.png')
openUse=image.load('tools/openUse.png')
saveUse=image.load('tools/saveUse.png')
eliUse=image.load('tools/bucketUse.png')

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

###setting up rect objects
canvasRect=Rect(150,80,900,500)

pencilRect=Rect(50,600,85,85) 
eraserRect=Rect(50,700,85,85)
sprayRect=Rect(150,600,85,85)
shapeRect=Rect(150,700,85,85)
lineRect=Rect(250,600,85,85)
rectRect=Rect(250,700,85,85)
brushRect=Rect(350,600,85,85)
eliRect=Rect(350,700,85,85)

undoRect=Rect(50,15,85,50)
redoRect=Rect(150,15,85,50)
openRect=Rect(1065,80,85,85)
saveRect=Rect(1065,180,85,85)

stampRect=Rect(750,610,350,175)

paletteRect=Rect(510,595,200,200)
colDisplayRect=Rect(460,595,30,200)

toolRect=Rect(50,600,385,185)
topRect=Rect(50,15,385,50)
openSaveRect=Rect(1065,80,85,185)


###displaying images
screen.blit(programBackground,(0,0))
screen.blit(paletteWheel,paletteRect)
draw.rect(screen,WHITE,canvasRect)
draw.rect(screen,WHITE,stampRect)

#setting initial values
click=False
rightClick=False
paletteSel=False
toolSel=False
topSel=False
openSave=False
running=True

endShape=False
pastScreen=False
mbStartCanvas=False
lineCopy=False
shapeDone=False
shapeUndoStep=False

tool='no tool' #tool selection default is none
omx,omy=0,0 #setting value 
size=5 #default size
col=0,0,0,255 #default colour black
r,g,b,a=0,0,0,0 #default values for rgb and alpha(a)
mx,my=0,0   #default values for mouse pos
sx,sy=0,0   #default value for starting position
empty=screen.subsurface(canvasRect).copy()  #default starting canvas
screenCap=empty     #original canvas 

colList=[(1,0,0,255),(0,1,0,255),(0,0,1,255),(1,1,0,255),(0,0,0,255)]
undoList=[empty] #undo when you press undo the most recent item added is blitted
redoList=[empty] #redo when you press redo the most recent item added is blitted
shapeList=[]     #coordinates for the shape tool
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
            
        if evt.type==MOUSEBUTTONDOWN:
            if evt.button==1:
                sx,sy=evt.pos               #starting position of tool
                click=True                  #mouse has been clicked
                print("mouse down")
                
            if canvasRect.collidepoint(mx,my):  #to see if the mouse was clicked on the canvas first
                mbStartCanvas=True
            else:
                mbStartCanvas=False
            if paletteRect.collidepoint(mx,my): #to see if user is selecting the colour palette
                paletteSel=True
            else:
                paleteSel=False
            if colDisplayRect.collidepoint(mx,my):
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

            if evt.button==3 and tool=='shape': #shape tool adding points for each click
                print(len(shapeList))
                if len(shapeList)>2:
                    shapeDone=True
                    shapeUndoStep=True
                    draw.polygon(screen,col,shapeList,size)
    
            if evt.button==4: #scrolling up increases thickness
                if size+1<11:
                    size+=1
            if evt.button==5: #scrolling down decreases thickness
                if size-1>0:
                    size-=1            

        if evt.type==MOUSEBUTTONUP:
            if evt.button==1:
                if mbStartCanvas==True and tool!='no tool' and tool!='shape':
                    fwdScreen=screen.subsurface(canvasRect).copy()
                    undoList.append(fwdScreen)
                    
            if evt.button==1:
                if paletteRect.collidepoint(mx,my) and paletteSel: #displaying colours
                    colList.append(col)
                if len(colList)>5:
                    colList.pop(0)
                if colDisplayRect.collidepoint(mx,my) and colDisplay:
                    colPick=colList.index(col)
                    colList[colPick],colList[-1]=colList[-1],colList[colPick]
                    
            if tool=='shape' and shapeUndoStep:
                shapeUndoStep=False
                fwdScreen=screen.subsurface(canvasRect).copy()
                undoList.append(fwdScreen)
                
            if tool=='line':
                if evt.button==1:
                    screenCap=screen.subsurface(canvasRect).copy()
                    screen.blit(screenCap,(canvasRect))
                    screen.set_clip(canvasRect)
                    draw.line(screen,col,(sx,sy),(mx,my),size)
                    screenCap=screen.subsurface(canvasRect).copy()
                    screen.set_clip(None)

            if tool=='shape' and canvasRect.collidepoint(mx,my):
                if evt.button==1 and shapeDone==False:
                    shapeList.append(mouse.get_pos())
                    for term in range(len(shapeList)):
                        draw.circle(screen,col,shapeList[term],1)
                if shapeDone:
                    shapeList*=0
                    shapeDone=False        
            if openSave:
                fwdScreen=screen.subsurface(canvasRect).copy()
                undoList.append(fwdScreen)
                
            click=False
            paletteSel=False
            print("mouse up")

               
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()

###drawing the rectangles
    
    screen.blit(pencilIcon,(pencilRect))
    screen.blit(eraserIcon,(eraserRect))
    screen.blit(sprayIcon,(sprayRect))
    screen.blit(shapeIcon,(shapeRect))
    screen.blit(lineIcon,(lineRect))
    screen.blit(rectIcon,(rectRect))
    screen.blit(brushIcon,(brushRect))
    screen.blit(undoIcon,(undoRect))
    screen.blit(redoIcon,(redoRect))
    screen.blit(openIcon,(openRect))
    screen.blit(saveIcon,(saveRect))
    screen.blit(eliIcon,(eliRect))
    
###hovering over objects
    if pencilRect.collidepoint(mx,my):
        screen.blit(hover,(pencilRect))
    if eraserRect.collidepoint(mx,my):
        screen.blit(hover,(eraserRect))
    if sprayRect.collidepoint(mx,my):
        screen.blit(hover,(sprayRect))
    if shapeRect.collidepoint(mx,my):
        screen.blit(hover,(shapeRect))
    if lineRect.collidepoint(mx,my):
        screen.blit(hover,(lineRect))
    if rectRect.collidepoint(mx,my):
        screen.blit(hover,(rectRect))
    if brushRect.collidepoint(mx,my):
        screen.blit(hover,(brushRect))
    if eliRect.collidepoint(mx,my):
        screen.blit(hover,(eliRect))
        
    if undoRect.collidepoint(mx,my):
        screen.blit(hover2,(undoRect))
    if redoRect.collidepoint(mx,my):
        screen.blit(hover2,(redoRect))
    if openRect.collidepoint(mx,my):
        screen.blit(hover,(openRect))
    if saveRect.collidepoint(mx,my):
        screen.blit(hover,(saveRect))
###selecting 
    if toolSel:
        if mb[0]==1 and pencilRect.collidepoint(mx,my):
            tool='pencil'
            pencilIcon=pencilUse
            eraserIcon=eraserRest
            sprayIcon=sprayRest
            shapeIcon=shapeRest
            lineIcon=lineRest
            rectIcon=rectRest
            brushIcon=brushRest
            eliIcon=eliRest
        if mb[0]==1 and eraserRect.collidepoint(mx,my):
            tool='eraser'
            pencilIcon=pencilRest
            eraserIcon=eraserUse
            sprayIcon=sprayRest
            shapeIcon=shapeRest
            lineIcon=lineRest
            rectIcon=rectRest
            brushIcon=brushRest
            eliIcon=eliRest
        if mb[0]==1 and sprayRect.collidepoint(mx,my):
            tool='spray'
            pencilIcon=pencilRest
            eraserIcon=eraserRest
            sprayIcon=sprayUse
            shapeIcon=shapeRest
            lineIcon=lineRest
            rectIcon=rectRest
            brushIcon=brushRest
            eliIcon=eliRest
        if mb[0]==1 and shapeRect.collidepoint(mx,my):
            tool='shape'
            pencilIcon=pencilRest
            eraserIcon=eraserRest
            sprayIcon=sprayRest
            shapeIcon=shapeUse
            lineIcon=lineRest
            rectIcon=rectRest
            brushIcon=brushRest
            eliIcon=eliRest
        if mb[0]==1 and lineRect.collidepoint(mx,my):
            tool='line'
            pencilIcon=pencilRest
            eraserIcon=eraserRest
            sprayIcon=sprayRest
            shapeIcon=shapeRest
            lineIcon=lineUse
            rectIcon=rectRest
            brushIcon=brushRest
            eliIcon=eliRest
        if mb[0]==1 and rectRect.collidepoint(mx,my):
            tool='rect'
            pencilIcon=pencilRest
            eraserIcon=eraserRest
            sprayIcon=sprayRest
            shapeIcon=shapeRest
            lineIcon=lineRest
            rectIcon=rectUse
            brushIcon=brushRest
            eliIcon=eliRest
        if mb[0]==1 and brushRect.collidepoint(mx,my):
            tool='brush'
            pencilIcon=pencilRest
            eraserIcon=eraserRest
            sprayIcon=sprayRest
            shapeIcon=shapeRest
            lineIcon=lineRest
            rectIcon=rectUse
            brushIcon=brushUse
            eliIcon=eliRest
        if mb[0]==1 and eliRect.collidepoint(mx,my):
            tool='eli'
            pencilIcon=pencilRest
            eraserIcon=eraserRest
            sprayIcon=sprayRest
            shapeIcon=shapeRest
            lineIcon=lineRest
            rectIcon=rectRest
            brushIcon=brushRest
            eliIcon=eliUse
            
###flashing for buttons
    if mb[0]==1 and redoRect.collidepoint(mx,my):
        redoIcon=redoUse
    else:
        redoIcon=redoRest
    if mb[0]==1 and undoRect.collidepoint(mx,my):
        undoIcon=undoUse
    else:
        undoIcon=undoRest
        
    if click and openRect.collidepoint(mx,my):
        openIcon=openUse
    else:
        openIcon=openRest
    if click and saveRect.collidepoint(mx,my):
        saveIcon=saveUse
    else:
        saveIcon=saveRest

###using buttons
    if topSel: #to see if the cursor is in the top button range
        if mb[0]==1 and undoRect.collidepoint(mx,my):
            if len(undoList)>1:         #base canvas cant be deleted
                undone=undoList[-1]     #undo step capture saved
                undoList.pop()          #removing the undo step
                screen.blit(undoList[-1],canvasRect) #putting the previous screencap on canvas
                redoList.append(undone) #adding the removed capture
                pastScreen=True         #current canvas exists in the past
                topSel=False            #setting back to default value
                screenCap=screen.subsurface(canvasRect).copy()
        if mb[0]==1 and redoRect.collidepoint(mx,my):
            if len(redoList)>1:         #base canvas cant be deleted
                redone=redoList[-1]     #redo step capture saved
                screen.blit(redoList[-1],canvasRect) #putting the redone screencap on canvas
                redoList.pop()          #removing the redo step and
                undoList.append(redone) #adding it to the undo step
                topSel=False            #setting back to default value
                screenCap=screen.subsurface(canvasRect).copy()

    if openSave:
        if mb[0]==1 and openRect.collidepoint(mx,my):
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
                    factorH=heightPic/500   #image is scalled so the hiehgt fits on canvas, 
                    myPic=transform.scale(myPic,(int(widthPic/factorH),int(heightPic/factorH)))
                    widthPic=myPic.get_width()
                    heightPic=myPic.get_height()
                distX=(900-widthPic)/2 #calculating distance to be moved to the right to center
                distY=(500-heightPic)/2 #calculating distance to be moved to down to center
                screen.blit(myPic,(150+distX,80+distY,900,500)) #putting image in the center of canvas
                print('opened',fName)
                screen.set_clip(None)
            except:
                print('loading error')

        if mb[0]==1 and saveRect.collidepoint(mx,my):
            print('hi')
            try:
                fName=filedialog.asksaveasfilename(defaultextension='.png')
                image.save(screen.subsurface(canvasRect).copy(),fName)
                print('saved as',fName)
            except:
                print('saving error')
    
###colour picking
    if mb[0]==1 and paletteRect.collidepoint(mx,my) and paletteSel:
        col=screen.get_at((mx,my))
        r,g,b,a=screen.get_at((mx,my))

###displaying colours
    #screen.blit(colDisplay,colDisplayRect)
    for rectCol in range(5):
        draw.rect(screen,(colList[rectCol]),(460,755-40*rectCol,30,40))

    if mb[0]==1 and colDisplayRect.collidepoint(mx,my) and colDisplay:
        col=screen.get_at((mx,my))
        
    screen.blit(colDisplayFrame,colDisplayRect)

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


###using tool
    if mb[0]==1 and canvasRect.collidepoint(mx,my) or mb[0]==1 and mbStartCanvas:
        screen.set_clip(canvasRect)
        if tool=='pencil':
            if size>5:
                size=5
            draw.line(screen,col,(omx,omy),(mx,my),size)
        if tool=='eraser':
            draw.circle(screen,WHITE,(mx,my),size)
        if tool=='spray':
            draw.circle(screen,col,(sprayX,sprayY),2) #outer circle
            draw.circle(screen,col,(sprayX2,sprayY2),3) #middle circle
            draw.circle(screen,col,(sprayX3,sprayY3),4) #inner circle
            
        if tool=='line':
            screen.blit(screenCap,canvasRect)
            draw.line(screen,col,(sx,sy),(mx,my),size)
            
        if tool=='rect':
            draw.rect(screen,col,(sx,sy,mx-sx,my-sx))
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
                    
        if pastScreen: #if there is drawing on the canvas when it is done in the past/undo steps
            redoList*=0 #clearing the list
            redoList.append(empty) #adding the empty canvas
            
        
        screen.set_clip(None)
    
    display.flip()
    #print(tool,r,g,b,a)
      
    omx=mx
    omy=my
quit()
