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
        printf(" %d ", head->val);
        head = head->next;
    }
}

struct ListNode* oddEvenList(struct ListNode* head) {
    
    if (head == NULL || head->next == NULL || head->next->next == NULL) return head;

    struct ListNode *head_odd = head, *head_even = head, *curr = head, *new_head = head, *new_head_odd=head;


    curr = curr->next; 
    new_head_odd = curr; //print_list(new_head_odd);
    head_odd = curr;

    while (curr->next) {
        head_even->next = curr->next; 
        head_even = head_even->next;

        curr = curr->next;

        if (curr && curr->next) {
            head_odd->next = curr->next;
            head_odd = head_odd->next;

        curr = curr->next;
        } else {
            head_odd->next = NULL;
            break;
        }

        //print_list(new_head);
    }

    head_even->next = new_head_odd;

    return new_head;
}