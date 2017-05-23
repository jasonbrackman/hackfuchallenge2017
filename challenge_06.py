# looking through the decryptor file there is some hex numbers.
# --> 4c 2e 52 6f 6e 20 48 75 62 62 61 72 64 --> L.Ron Hubbard
# instructions:
# So I hope you know how to reverse engineer
# [FBecause I am looking for a file to make the next stage appear!
# [FFind the key or rename the file.
# [FPersevere through the struggle, and it will all be worthile.
# =====================================================================
# >>>.......Searching for target file in current Directory.........
# [!] File Not Found...
# [-] Find the key or rename the file,
# [-] both of these will get you to the next stage
# Final_Stage
# [+] successfully decrypted final stage
# [+] One step closer!
# failed to decrypt final stage
#
# .--.                   .            .--.                      .
# |   : o               _|_   o       |   :                    _|_
# |   | .  .-.  .--. .-. |    .  .-.  |   | .-. .-..--..  ..,-. |  .-. .--.
# |   ; | (   ) |  |(.-' |    | (     |   ;(.-'(   |   |  ||   )| (   )|
# '--'-' `-`-'`-'  `-`--'`-'-' `-`-'  '--'  `--'`-''   `--||`-' `-'`-' '
#                                                         ;|
#                                                      `-' '
#  0000000000400c21 <create_decrypt_key>:
#
#   400c21:   55                      push   %rbp
#   400c22:   48 89 e5                mov    %rsp,%rbp          ;lines point back to the main() func pointer
#   400c25:   48 83 ec 60             sub    $0x60,%rsp         ;Creating 96 bytes of stack space, within the frame,
#                                                               ;for locals
#   400c29:   48 89 7d a8             mov    %rdi,-0x58(%rbp)   ;first argument passed in (I think) - although maybe its
#                                                               ;an array being setup to exist at rbp[-58]
#   400c2d:   64 48 8b 04 25 28 00    mov    %fs:0x28,%rax      ;storing a special sentinel stack-guard value, and the
#                                                               ;code is performing a stack-guard check.
#                                                               ;Thinking more on this -- this is likely the weird
#                                                               ;alphabet repeated in the earlier part of the program.
#                                                               ; maybe?
#   400c34:   00 00
#   400c36:   48 89 45 f8             mov    %rax,-0x8(%rbp)    ; hold onto the pointer on the stack at rbp[-8]
#   400c3a:   31 c0                   xor    %eax,%eax          ; clear out a 32bit register
#   400c3c:   c7 45 c0 00 00 00 00    movl   $0x0,-0x40(%rbp)   ; store zero = p
#   400c43:   c7 45 c4 01 00 00 00    movl   $0x1,-0x3c(%rbp)   ; store 1    = h
#   400c4a:   c7 45 c8 03 00 00 00    movl   $0x3,-0x38(%rbp)   ; store 3    = a
#   400c51:   c7 45 cc 05 00 00 00    movl   $0x5,-0x34(%rbp)   ; store 5    = n
#   400c58:   c7 45 d0 08 00 00 00    movl   $0x8,-0x30(%rbp)   ; store 8    = t
#   400c5f:   c7 45 d4 0d 00 00 00    movl   $0xd,-0x2c(%rbp)   ; store 13   = o
#   400c66:   c7 45 d8 15 00 00 00    movl   $0x15,-0x28(%rbp)  ; store 21   = m
#   400c6d:   c7 45 dc 22 00 00 00    movl   $0x22,-0x24(%rbp)  ; store 34   = -
#   400c74:   c7 45 e0 37 00 00 00    movl   $0x37,-0x20(%rbp)  ; store 55   = k
#   400c7b:   c7 45 e4 59 00 00 00    movl   $0x59,-0x1c(%rbp)  ; store 89   = e
#   400c82:   c7 45 e8 90 00 00 00    movl   $0x90,-0x18(%rbp)  ; store 144  = y
#   400c89:   c7 45 b8 00 00 00 00    movl   $0x0,-0x48(%rbp)   ; store zero  -- sentinel maybe? used to loop over
#                                                                                an area from 0 <= 10 (11 times)

#   400c90:   eb 2b                   jmp    400cbd <create_decrypt_key+0x9c> ; Enter into a control loop **

#   400c92:   8b 45 b8                mov    -0x48(%rbp),%eax   ; put sentinel to %eax
#   400c95:   48 98                   cltq                      ; convert long to a quad (? not sure)

#   400c97:   8b 44 85 c0             mov    -0x40(%rbp,%rax,4),%eax ; fill the eax with something from the location
#                                                                      specified - moving through each of the stored
#                                                                      numbers.
#   400c9b:   89 45 bc                mov    %eax,-0x44(%rbp)   ; work with the current number depending on iteration
#   400c9e:   8b 45 b8                mov    -0x48(%rbp),%eax   ; put sentinel back to eax
#   400ca1:   48 63 d0                movslq %eax,%rdx          ; store sentinel in a 64bit register
#   400ca4:   48 8b 45 a8             mov    -0x58(%rbp),%rax   ; first letter from passed in arg added to return var
#   400ca8:   48 01 c2                add    %rax,%rdx          ; add the sentinel value to the letter value?
#   400cab:   8b 45 bc                mov    -0x44(%rbp),%eax   ; item in storage is placed into a 32bit register
#   400cae:   48 98                   cltq                      ; in place 64bit conversion
#   400cb0:   0f b6 80 00 21 60 00    movzbl 0x602100(%rax),%eax; move a 1 byte item (??) to the 4 byte eax
#   400cb7:   88 02                   mov    %al,(%rdx)         ; move the low 8bits to rdx address?

#   400cb9:   83 45 b8 01             addl   $0x1,-0x48(%rbp)   ; add one to the sentinel


#   400cbd:   83 7d b8 0a             cmpl   $0xa,-0x48(%rbp)   ; ** control of the loop: is rbp[-48] <= 10
#   400cc1:   7e cf                   jle    400c92 <create_decrypt_key+0x71> ; if result is less than or equal to 0xa
#                                                               ;
#                                                               ; I think at this point the Phantom-Key is pulled out
#                                                               ;
#   400cc3:   48 8b 45 a8             mov    -0x58(%rbp),%rax   ; load pointer to the array into the 64bit register
#   400cc7:   48 83 c0 0b             add    $0xb,%rax          ; add 11 to rax
#   400ccb:   c6 00 00                movb   $0x0,(%rax)        ; move the low byte of zero to rax.
#   400cce:   48 8b 45 f8             mov    -0x8(%rbp),%rax    ; Moving the pointer defined earlier back to the rax?
#                                                               ; ... i think?
#   400cd2:   64 48 33 04 25 28 00    xor    %fs:0x28,%rax      ; compare the data to the rax
#   400cd9:   00 00
#   400cdb:   74 05                   je     400ce2 <create_decrypt_key+0xc1> ; if password found
#   400cdd:   e8 0e fb ff ff          callq  4007f0 <__stack_chk_fail@plt>
#   400ce2:   c9                      leaveq
#   400ce3:   c3                      retq
import os

import challenge_00


def decrypt_message(passkey):
    infile_ = os.path.abspath('./Challenges/Challenge 6/solution.txt.enc')
    outfile_ = os.path.abspath('./Challenges/Challenge 6/generated_content/solution.txt')

    challenge_00.decrypt_openssl(infile=infile_, outfile=outfile_, passphrase=passkey)

#  Used the debugger edb on Linux virtual machine one more time, found: phantom_bits
#  Changed time on my host (this changed it in the virtual machine) to be the death date of L. Ron Hubbard
#  revealed:

passkey = 'hackfusummonthedemonatyourperilitisnotintelligentactuallyitsferal'
decrypt_message(passkey)
