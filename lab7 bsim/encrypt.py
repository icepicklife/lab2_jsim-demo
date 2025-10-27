def encrypt_stream(key_block, plaintext_block):
    
    m = key_block[0]
    keystream = key_block[1:]
    
    n = plaintext_block[0]
    plaintext = plaintext_block[1:]
    
    encrypted_list = []
    
    for i in range(n):
        
        # Calculate the key index with wrap-around
        key_index = i % m
        
        # Get the two values for XOR
        current_key = keystream[key_index]
        current_plaintext = plaintext[i]
        
        # XOR operation 
        encrypted_val = current_plaintext ^ current_key
        
        encrypted_list.append(encrypted_val)
        
    return encrypted_list