;essentilly calling int 10h when ah has 0eh will allow the system to read all of the messages from the different variables into the buffer --> then using times (which I think reads from the start of the buffer) you can print it out (plus dw 0xaa55)

;https://arjunsreedharan.org/post/99370248137/kernels-201-lets-write-a-kernel-with-keyboard

;The interrupt int 16h 00h not only reads from the keyboard buffer, but it also removes the key read from the buffer and stores the ASCII format in AL. That way, the buffer won't continue to fill and fill.


org 0x7c00
;Note: big hint is that the buffer starts at 0000:041eh

mov si, output
mov ah, 0eh ;write character in TTY mode

msgloop:
mov al, [si] ;al is the lower 8 bits of the edx register (dx is the lower 16 bits)
cmp al, 0 ;searches for null ended string
je keyloop
int 10h
inc si
jmp msgloop

keyloop:
mov ah, 01h
int 16h
cmp al, 0dh ;CR check
jz keyloop
je endmsgloop
mov ah, 00h
int 16h

mov ah, 0eh
int 10h
mov dx, 03f8h
out dx, al
jmp keyloop


endmsgloop:
output db 0AH,'Type characters and press <ENTER>:',0AH,0DH,0
times 510-($-$$) db 0 ; $ = current address, $$ = first address of current section, $-$$ gives offset from the start to the address of the currently executed instruction, subtract that value from 510 and you get the offset of the address of the currently executed instruction to the 510th byte --> the times directive will use this offset to pad that number of bytes up to the 510th byte with zeros. 
dw 0xaa55










