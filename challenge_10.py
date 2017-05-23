"""
Interesting items to test against:
- 4550
- 5a4d
- c8
- dead
- beef
- feedf00d


          3041                 db  0Eh
.data:00403042                 db  17h
.data:00403043                 db  12h
.data:00403044                 db    3
.data:00403045                 db    1
.data:00403046                 db  10h
.data:00403047                 db  18h
.data:00403048                 db    7
.data:00403049                 db  0Bh
.data:0040304A                 db  5Bh ; [
.data:0040304B                 db  5Ch ; \
.data:0040304C                 db  51h ; Q
.data:0040304D                 db  5Fh ; _
.data:0040304E                 db  44h ; D
.data:0040304F                 db  43h ; C
.data:00403050                 db  5Eh ; ^
.data:00403051                 db  2Dh ; -
.data:00403052                 db  47h ; G
.data:00403053                 db  56h ; V
.data:00403054                 db  5Bh ; [
.data:00403055                 db  45h ; E
.data:00403056                 db  5Dh ; ]
.data:00403057                 db  5Bh ; [
.data:00403058                 db  2Ch ; ,
.data:00403059                 db  4Ch ; L
.data:0040305A                 db  44h ; D
.data:0040305B                 db  5Ch ; \
.data:0040305C                 db  51h ; Q
.data:0040305D                 db  43h ; C
.data:0040305E                 db  45h ; E
.data:0040305F                 db  58h ; X
.data:00403060                 db  43h ; C
.data:00403061                 db  19h
.data:00403062                 db  0Ah
.data:00403063                 db  1Ch
.data:00403064                 db  18h
.data:00403065                 db  13h
.data:00403066                 db  11h
.data:00403067                 db  0Ah
.data:00403068                 db    0
.data:00403069                 db    7
.data:0040306A                 db  0Bh
.data:0040306B                 db  44h ; D
.data:0040306C                 db  55h ; U
.data:0040306D                 db  46h ; F
.data:0040306E                 db  55h ; U
.data:0040306F                 db  42h ; B
.data:00403070                 db  43h ; C
.data:00403071                 db  59h ; Y
.data:00403072                 db  2Ch ; ,
.data:00403073                 db  47h ; G
.data:00403074                 db  58h ; X
.data:00403075                 db  55h ; U
.data:00403076                 db  44h ; D
.data:00403077                 db  48h ; H
.data:00403078                 db  58h ; X
.data:00403079                 db  30h ; 0
.data:0040307A                 db  59h ; Y
.data:0040307B                 db  42h ; B
.data:0040307C                 db  55h ; U

     :00403041 aQ_dcGvELdQcexc db 0Eh,17h,12h,3,1,10h,18h,7,0Bh,
                                  '[\Q_DC^-GV[E][,LD\QCEXC',
                                   19h, 0Ah
.data:00403041                 db 1Ch,18h,13h,11h,0Ah
.data:00403041                 db 0,7,0Bh,'DUFUBCY,GXUDHX0YBU'
"""
import os

import challenge_00

x = 'DUFUBCY,GXUDHX0YBU'
y = '-e-e------e------e'
z = 'never-----en----re'
a = 'never     en- --re'

x = '112211221122112211221122112211112211221122112211221122E9174000'


def decrypt_message(passkey):
    infile_ = os.path.abspath('./Challenges/Challenge 10/solution.txt.enc')
    outfile_ = os.path.abspath('./Challenges/Challenge 10/generated_content/solution.txt')

    challenge_00.decrypt_openssl(infile=infile_, outfile=outfile_, passphrase=passkey)

if __name__ == "__main__":
    passkey = 'hackfutwinkleoutnowfoullittlestarwehavenointerestinwhatyouare'
    decrypt_message(passkey)