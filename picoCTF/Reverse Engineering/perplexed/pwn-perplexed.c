#include <stdio.h>
#include <string.h>

typedef unsigned char undefined8;
typedef unsigned int uint;

char pass[28];
char solved[28];
int num_solved = 0;

undefined8 check(char *param_1)
{
  size_t sVar1;
  undefined8 uVar2;
  size_t sVar3;
  char local_58 [36];
  uint local_34;
  uint local_30;
  // undefined4 local_2c;
  undefined8 local_2c;
  int local_28;
  uint local_24;
  int local_20;
  int local_1c;
  
  sVar1 = strlen(param_1);
  if (sVar1 == 0x1b) {
    local_58[0] = -0x1f;
    local_58[1] = -0x59;
    local_58[2] = '\x1e';
    local_58[3] = -8;
    local_58[4] = 'u';
    local_58[5] = '#';
    local_58[6] = '{';
    local_58[7] = 'a';
    local_58[8] = -0x47;
    local_58[9] = -99;
    local_58[10] = -4;
    local_58[0xb] = 'Z';
    local_58[0xc] = '[';
    local_58[0xd] = -0x21;
    local_58[0xe] = 'i';
    local_58[0xf] = 0xd2;
    local_58[0x10] = -2;
    local_58[0x11] = '\x1b';
    local_58[0x12] = -0x13;
    local_58[0x13] = -0xc;
    local_58[0x14] = -0x13;
    local_58[0x15] = 'g';
    local_58[0x16] = -0xc;
    local_1c = 0;
    local_20 = 0;
    local_2c = 0;

    // for 0 to 22
    for (local_24 = 0; local_24 < 0x17; local_24 = local_24 + 1) {
      // for 0 to 7
      for (local_28 = 0; local_28 < 8; local_28 = local_28 + 1) {
        // set local_20 to 1 if its zero at the start of the iteration
        if (local_20 == 0) {
          local_20 = 1;
        }
        //  inner loop       = 1 << 7 - (0 to 7)
        local_30 = 1 << (7U - (char)local_28 & 0x1f);
        // 
        local_34 = 1 << (7U - (char)local_20 & 0x1f);
        if (0 < (int)((int)param_1[local_1c] & local_34) !=
            0 < (int)((int)local_58[(int)local_24] & local_30)) {
          // Incorrect
          num_solved = local_1c;
          return 1;
        }
        local_20 = local_20 + 1;
        if (local_20 == 8) {
          local_20 = 0;
          local_1c = local_1c + 1;
        }
        sVar3 = (size_t)local_1c;
        sVar1 = strlen(param_1);
        if (sVar3 == sVar1) {
          // Correct
          return 0;
        }
      }
    }
    uVar2 = 0;
  }
  else {
    // Incorrect
    printf("Incorrect (2)\n");    
    uVar2 = 1;
  }
  return uVar2;
}

int
main(void)
{
  int prev_num_solved = 0;
  undefined8 hash_test = 1;
  while (hash_test != 0)
  {
    for (char cut = 0x20; cut < 0x7f; ++cut)
    {
      if (num_solved > 0)
      {
        strncpy(pass, solved, num_solved);
      }

      memset(&pass[num_solved], 'A', sizeof(pass) - num_solved);
      pass[num_solved] = cut;
      pass[sizeof(pass)-1] = '\0';

      hash_test = check(pass);

      if (num_solved > prev_num_solved)
      {
        printf("Solved %d characters....\n", num_solved);
        memcpy(&solved, &pass, num_solved);
        prev_num_solved = num_solved;
      }

      if ((num_solved > 0) && (solved[num_solved-1] == '}'))
      {
        solved[num_solved] = '\0';
        printf("Flag: %s\n", solved);
        return 0;
      }
    }
  }

  return 0;
}