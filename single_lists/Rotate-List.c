/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* rotateRight(struct ListNode* head, int k) {
    if (head == NULL || head->next == NULL || k == 0) return head;

struct ListNode *looping = head, *end, *last_node = head, *new_head=head;
int length = 0;

//finding the length of the list
while(looping != NULL) {
    end = looping;
    looping = looping->next;
    length++;
}

int new_k = k % length;

if (new_k == 0) return head;

//printf("\n length = %d,  new_k = %d", length, new_k);

for (int i = (length - new_k-1); i>0; i--) {
    last_node = last_node->next;
    //printf("\n inside for   last_node->val = %d", last_node->val);
}
//printf("\n last_node->val = %d", last_node->val);

    new_head = last_node->next;
    last_node->next = NULL;
    end->next = head;


/* if (last_node->next == NULL ) {
            new_head = last_node;
            last_node->next = head;
            curr = head;
            while (curr->next != new_head) {
                curr = curr->next;
            }
            curr->next = NULL;
        } else 
    if (last_node == head) {
            return head;
        } else {
            new_head = last_node->next;
            last_node->next = NULL;
        }
*/

// taking too much time for k = 2 000 000 000, looping around the list until reaching the k
/*    struct ListNode *curr= head, *last_node = head, *new_head=head;

    while (k>0) {
        if (last_node->next == NULL) {
            last_node = head;
        } else {
            last_node = last_node->next;
        }
        k--;
    }

    //printf("\n last_node->val = %d", last_node->val);
    
    if (last_node->next == NULL ) {
            new_head = last_node;
            last_node->next = head;
            curr = head;
            while (curr->next != new_head) {
                curr = curr->next;
            }
            curr->next = NULL;
        } else if (last_node == head) {
            return head;
        } else {
            new_head = last_node->next;
            last_node->next = NULL;
            curr = new_head;
            while (curr->next != NULL) {
                curr = curr->next;
            }
            curr->next = head;
        }
*/


// bruteforce
    /*
    struct ListNode *old_head = head, *end = head;
    while (k > 0) {

        while(head->next != NULL) {
            end = head;
            head = head->next;
        }
        end->next = NULL;
        head->next = old_head;
        old_head = head;

        k--;
    }
*/
    return new_head;
}