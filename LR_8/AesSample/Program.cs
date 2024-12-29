using System;
using System.Security.Cryptography;
using System.Text;

public class AesEcbExample
{
    public static byte[] EncryptEcb(byte[] data, byte[] key)
    {
        using (Aes aes = Aes.Create())
        {
            aes.Key = key;
            aes.Mode = CipherMode.ECB; 
            aes.Padding = PaddingMode.PKCS7; 

            using (var encryptor = aes.CreateEncryptor())
            {
                return encryptor.TransformFinalBlock(data, 0, data.Length);
            }
        }
    }

    public static byte[] DecryptEcb(byte[] data, byte[] key)
    {
        using (Aes aes = Aes.Create())
        {
            aes.Key = key;
            aes.Mode = CipherMode.ECB;
            aes.Padding = PaddingMode.PKCS7;

            using (var decryptor = aes.CreateDecryptor())
            {
                return decryptor.TransformFinalBlock(data, 0, data.Length);
            }
        }
    }

    public static void Main()
    {
        byte[] key = new byte[16] { 0x9f, 0xbd, 0xe6, 0x4f, 0xad, 0xe1, 0xf3, 0x9d, 0x5e, 0x53, 0x7f, 0xbb, 0x92, 0x96, 0x85, 0x10 };

        string plainText = "Hello it s Anton Panakov"; 

        byte[] encryptedData = EncryptEcb(Encoding.Default.GetBytes(plainText), key);

        Console.WriteLine("The encrypted data is :");
        Console.WriteLine(Convert.ToBase64String(encryptedData)); 

        byte[] decryptedData = DecryptEcb(encryptedData, key);

        Console.WriteLine("The clear data is :");
        Console.WriteLine(Encoding.Default.GetString(decryptedData));
    }
}