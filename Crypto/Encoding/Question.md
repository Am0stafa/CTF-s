### The Question:

Now you've got the hang of the various encodings you'll be encountering, let's have a look at automating it.

Can you pass all 100 levels to get the flag?

The 13377.py file attached below is the source code for what's running on the server. The solution.py file provides the start of a solution.

Connect at socket.cryptohack.org 13377

Challenge files:
  - 13377.py
  - solution.py

---

### Explanation:

This challenge tests your ability to automate the process of decoding various types of encoded messages. The server sends 100 different encoded messages, each using one of five encoding methods: base64, hex, rot13, bigint, or utf-8. Your task is to create a script that can:

1. Connect to the server using a socket connection
2. Receive JSON-encoded challenges
3. Determine the encoding type for each challenge
4. Decode the message correctly
5. Send the decoded message back to the server
6. Repeat this process 100 times to receive the flag

The challenge emphasizes several key skills:
- Socket programming for network communication
- JSON parsing and creation
- Implementing various decoding algorithms
- Automating a repetitive process
- Error handling and robust programming

