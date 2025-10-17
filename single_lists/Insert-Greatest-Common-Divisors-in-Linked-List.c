/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

// Function to return gcd of a and b
int gcd(int a, int b)
{
    // Find Minimum of a and b
    int result = ((a < b) ? a : b);
    while (result > 0) {
        // Check if both a and b are divisible by result
        if (a % result == 0 && b % result == 0) {
            break;
        }
        result--;
    }
    // return gcd of a nd b
    return result;
}

struct ListNode* insertGreatestCommonDivisors(struct ListNode* head) {

    if (head == NULL || head->next == NULL) return head;
    struct ListNode *curr=head, *prev=NULL, *next=NULL;
    //if (head && head->next) printf("\n gcd = %d", gcd(head->val, head->next->val));

    //for first and second nodes
    if (curr && curr->next) {
        prev = curr;
        next = curr->next;
        curr->next = (struct ListNode*) malloc(sizeof(struct ListNode));
        curr = curr->next;
        curr->val = gcd(prev->val, next->val);
        curr->next = next;
        curr = next;
    } else return head;

    while (curr && curr->next) {        
        prev = curr;
        next = curr->next;
        curr->next = (struct ListNode*) malloc(sizeof(struct ListNode));
        curr = curr->next;
        curr->val = gcd(prev->val, next->val);
        curr->next = next;
        curr = next;    
    }

return head;   
}