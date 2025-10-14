/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

void print_list(struct ListNode *head) {
    printf("\n List:");
    while (head) {
        printf(" %d ", head->val);
        head = head->next;
    }
}

struct ListNode* mergeInBetween(struct ListNode* list1, int a, int b, struct ListNode* list2){

    struct ListNode* head1 = list1, *prev = NULL;
    int idx = 0;

    while (head1) {
        if (idx < a) {
            //printf("\n <a idx = %d", idx);
            prev = head1;
            head1 = head1->next;
            idx++;
        } else if ( idx <=b) {
            //printf("\n <b idx = %d", idx);
            head1 = head1->next;
            idx++;
        }
        if (idx == b){    
            //printf("\n <b idx = %d", idx);
            prev->next = list2;
            while (list2->next != NULL) {
                list2 = list2->next;
            }
            list2->next = head1->next;
            break;
        }
    }

    //print_list(list1);

    return list1;
}