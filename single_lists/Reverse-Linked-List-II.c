/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

void print_list(struct ListNode* head) {
    printf("\n List: ");
    while (head) {
        printf(" %d", head->val);
        head = head->next;
    }
}

struct ListNode* inverseList(struct ListNode* head) {
    struct ListNode *new_head=head, *prev=NULL, *curr=head, *next=head;

    next = next->next;

    while (next) {
        curr->next = prev;
        prev = curr;
        curr = next;
        new_head = curr;
        next = next->next;
    }

    curr->next = prev;

    //printf("\n new_head = %d", new_head->val);
    //print_list(new_head);
    return new_head;
}

struct ListNode* reverseBetween(struct ListNode* head, int left, int right) {
 
    if (head == NULL || head->next == NULL) return head;
    struct ListNode *new_head = head, *before = head, *after = head, *int_head=head;
    int idx_left = 1, idx_right = 1;

//printf("\n head = %d", head->val);
//inverseList(head);
    while (head) {
        if (idx_left == left) {
            int_head = head;
            //printf("\n int_head = %d", int_head->val);
            while (head) {
                if (idx_right == right) {
                    //printf("\n out_head = %d", head->val);
                    after = head->next;
                    head->next = NULL;

                    int_head = inverseList(int_head);//printf("\n   int_head = %d,  before = %d", int_head->val, before->val);
                    if (idx_left > 1) {                        
                        before->next = int_head;
                    } else {                        
                        new_head = int_head;                        
                    }
                    
                    if (after == NULL) {//printf ("   fff = %p ", after); printf("\n new_head = %d", new_head->val);
                        return new_head;
                        }
                    while(int_head->next) {
                        int_head = int_head->next;
                    }
                    int_head->next = after;
                    return new_head;
                } else {
                    head = head->next;
                    idx_right++;
                }
            }
        } else {
            before = head;
            head = head->next;
            idx_left++;
            idx_right++;
        }
    }
    
    return new_head;
}