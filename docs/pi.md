# 3.14

## SSH PI

I was listening to an episode of [The Real Python podcast](https://realpython.com/podcasts/rpp/) and there was a brief conversation about remote development on a raspberry pi. This is what got me thinking about improving my current workflow I'm making updates to my stock bot. I'm running my pi headless and whenever I want to run test or make updates I find myself dropping into `vim`. Nothing wrong with using `vim` but it can be slow and cumbersome when you are looking to make swift changes and updates. So, what to do? 

**[REMOTE DEVELOPMENT WITH VS CODE](https://code.visualstudio.com/docs/remote/remote-overview)**. Yup! If you have yet to try remote dev with vs code, I highly recommend you give it a try. All you is needed is two computers and root level access on both. From there you can modify and make updates where necessary.

I used this [link](https://medium.com/@pythonpow/remote-development-on-a-raspberry-pi-with-ssh-and-vscode-a23388e24bc7) to setup my environments and seamlessly remote into my raspberry

## Private Key Cryptography - PKC

Sooooo PKC is the shit! You get TWO EXTREMELY LONG prime numbers - these are going to be your private keys - and combine them. Those combined prime numbers will be your public key. So, now you can assign that prime number to a txt message. Then send it out into the wild, across the internet, into your receivers hands safely. Ah! But keep in mind that in order to read (decrypt) the txt message you need th other large prime number to read it. If another person try’s to read your message they will need the other large prime number (private key) to decrypt the message.... fuckin’ PKC. Cool shit