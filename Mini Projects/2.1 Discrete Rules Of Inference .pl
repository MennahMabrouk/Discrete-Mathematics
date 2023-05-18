% Define the mapping between English phrases and propositional logic symbols

% Predicate for converting nouns
noun(noun1, p).
noun(noun2, q).
noun(noun3, r).
noun(noun4, s).
% Add more nouns as needed

% Predicate for converting verbs
verb(verb1, 'is').
verb(verb2, 'have').
verb(verb3, 'absent').
% Add more verbs as needed

% Predicate for converting sentences to propositional logic
convert_paragraph(Paragraph, Conclusion) :-
    % Split the paragraph into sentences
    split_string(Paragraph, '. ', '', Sentences),
    % Convert each sentence to its propositional logic
    convert_sentences(Sentences, LogicList),
    % Concatenate the logic of all sentences
    atomic_list_concat(LogicList, ' ', Logic),
    % Extract the conclusion
    extract_conclusion(Logic, Conclusion).

% Convert a list of sentences to propositional logic
convert_sentences([], []).
convert_sentences([Sentence | Rest], [Logic | RestLogic]) :-
    convert_sentence(Sentence, Logic),
    convert_sentences(Rest, RestLogic).

% Convert a sentence to propositional logic
convert_sentence(Sentence, Logic) :-
    % Split the sentence into words
    split_string(Sentence, ' ', '', Words),
    % Convert each word to its propositional logic symbol
    convert_words(Words, LogicList),
    % Concatenate the logic symbols into a single string
    atomic_list_concat(LogicList, ' ', Logic).

% Convert a list of words to propositional logic
convert_words([], []).
convert_words([Word | Rest], [Logic | RestLogic]) :-
    convert_word(Word, Logic),
    convert_words(Rest, RestLogic).

% Convert a word to its propositional logic symbol
convert_word(Word, Logic) :-
    noun(Word, Logic).
convert_word(Word, Logic) :-
    verb(Word, Logic).
% Add more word conversions as needed

% Extract the conclusion
extract_conclusion(Logic, Conclusion) :-
    % Split the logic string into individual parts
    split_string(Logic, ' ', '', Parts),
    % Find the part containing "Therefore" or "Conclusion:"
    (member(Conclusion, Parts), sub_string(Conclusion, _, _, _, 'Therefore'));
    (member(Conclusion, Parts), sub_string(Conclusion, _, _, _, 'Conclusion:')).

% Additional Rules of Inference

% Modus Ponens
inference_rule(modus_ponens, [A, B | _], B) :-
    A =.. [-> | _].

% Modus Tollens
inference_rule(modus_tollens, [~B, A | _], ~A) :-
    A =.. [-> | _].

% Disjunctive Syllogism
inference_rule(disjunctive_syllogism, [A v B, ~A | _], B).

% Example usage:
% ?- inference_rule(modus_ponens, [p, q], Conclusion).
% Conclusion = q
% ?- inference_rule(modus_tollens, [~q, p], Conclusion).
% Conclusion = ~p
% ?- inference_rule(disjunctive_syllogism, [p v q, ~p], Conclusion).
% Conclusion = q
